import os
import subprocess
import glob
from typing import Any
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain_experimental.llm_bash.bash import BashProcess
from langchain_community.tools.shell import ShellTool
from langchain.tools import BaseTool

# Initialize ShellTool using BashProcess
bash_process = BashProcess()
shell_tool = ShellTool(bash_process=bash_process)

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Check if API key is loaded
if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY environment variable is not set.")
    print("Please set it in a .env file or as an environment variable.")
    print("Example .env file content: OPENAI_API_KEY=your-api-key-here")
    import sys
    sys.exit(1)
else:
    print(f"API key loaded: {OPENAI_API_KEY[:5]}...")

# Function to execute shell commands safely
def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else f"Error: {result.stderr.strip()}"
    except Exception as e:
        return str(e)

# Function to load documentation files into a vector store
def load_documentation_into_vectorstore(help_file='help.txt'):
    # Load the combined help file
    documents = []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    
    try:
        # Check if the file exists
        if not os.path.exists(help_file):
            print(f"File {help_file} does not exist. Please run 'python combine_docs.py' first.")
            return None
        
        # Load the combined help file
        print(f"Loading file: {help_file}")
        loader = TextLoader(help_file)
        file_documents = loader.load()
        
        print(f"Loaded {len(file_documents)} documents from {help_file}")
        
        if len(file_documents) == 0:
            print(f"No content found in {help_file}")
            return None
        
        # Split the document into chunks
        split_docs = text_splitter.split_documents(file_documents)
        documents.extend(split_docs)
        
        print(f"Split into {len(split_docs)} chunks from {help_file}")
        
        if len(documents) == 0:
            print("No documents to index")
            return None
        
    except Exception as e:
        print(f"Error loading {help_file}: {str(e)}")
        import traceback
        traceback.print_exc()
        return None
    
    try:
        # Create embeddings
        print("Creating embeddings...")
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        
        # Create vector store
        print(f"Creating vector store with {len(documents)} documents...")
        vectorstore = FAISS.from_documents(documents, embeddings)
        
        return vectorstore
    except Exception as e:
        print(f"Error creating vector store: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

# Function to search for relevant documentation
def search_documentation(vectorstore, query, k=5):
    # Search for relevant documents
    docs = vectorstore.similarity_search(query, k=k)
    
    # Format the results
    results = []
    for doc in docs:
        source = doc.metadata.get('source', 'Unknown')
        content = doc.page_content
        results.append(f"Source: {source}\n\n{content}\n\n")
    
    return "\n".join(results)

# Function to generate a command based on the user's prompt and relevant documentation
def generate_command(llm, prompt, relevant_docs):
    # Create a prompt for the LLM to generate a command
    system_message = """
    You are an assistant that helps users interact with the Lacework CLI. 
    Based on the user's request and the relevant documentation provided, 
    generate the appropriate Lacework CLI command.
    
    If you cannot determine the exact command, provide your best guess and explain why.
    """
    
    user_message = f"""
    User Request: {prompt}
    
    Relevant Documentation:
    {relevant_docs}
    
    Based on the above, what is the appropriate Lacework CLI command to fulfill the user's request?
    """
    
    # Generate the command
    response = llm.predict(system_message + "\n\n" + user_message)
    
    return response

# Custom tool for Lacework commands with vector search
class LaceworkVectorSearchTool(BaseTool):
    name: str = "lacework_vector_search"
    description: str = "Searches Lacework CLI documentation using vector search and generates appropriate commands."
    vectorstore: Any = Field(exclude=True)
    llm: Any = Field(exclude=True)
    
    def __init__(self, vectorstore, llm):
        super().__init__(vectorstore=vectorstore, llm=llm)
    
    def _run(self, query: str) -> str:
        # Search for relevant documentation
        relevant_docs = search_documentation(self.vectorstore, query)
        
        # Generate a command based on the query and relevant documentation
        command_suggestion = generate_command(self.llm, query, relevant_docs)
        
        # Return the relevant documentation and command suggestion
        return f"""
        Based on your query, here are the relevant Lacework CLI documentation sections:
        
        {relevant_docs}
        
        Suggested command:
        {command_suggestion}
        """
    
    def _arun(self, query: str) -> str:
        # For async support
        raise NotImplementedError("This tool does not support async")

# Custom tool for executing Lacework commands
class LaceworkExecutorTool(BaseTool):
    name: str = "lacework_executor"
    description: str = "Executes Lacework CLI commands."
    
    def _run(self, command: str) -> str:
        return run_shell_command(command)
    
    def _arun(self, command: str) -> str:
        # For async support
        raise NotImplementedError("This tool does not support async")

# Initialize OpenAI language model
llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

# Load documentation into vector store
print("Loading documentation into vector store...")
vectorstore = load_documentation_into_vectorstore()

if vectorstore is None:
    print("Failed to load documentation. Please check the error messages above.")
    import sys
    sys.exit(1)

print("Documentation loaded successfully!")

# Define tools for the agent
tools = [
    LaceworkVectorSearchTool(vectorstore, llm),
    LaceworkExecutorTool(),
    shell_tool  # Allows shell execution
]

# Initialize LangChain agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# FastAPI app setup
app = FastAPI()

# Define request model
class CommandRequest(BaseModel):
    command: str

# API endpoint to execute commands
@app.post("/execute/")
async def execute_command(request: CommandRequest):
    try:
        response = agent.run(request.command)
        return {"output": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Main entry point for running FastAPI
if __name__ == "__main__":
    import uvicorn
    import socket
    
    # Try to find an available port
    port = 8080
    max_port = 8090  # Try ports up to this number
    
    while port <= max_port:
        try:
            # Test if port is available
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.close()
            # If we get here, the port is available
            break
        except OSError:
            print(f"Port {port} is in use, trying next port...")
            port += 1
    
    if port > max_port:
        print("Could not find an available port. Please free up a port and try again.")
    else:
        print(f"Starting server on port {port}")
        uvicorn.run(app, host="0.0.0.0", port=port)
