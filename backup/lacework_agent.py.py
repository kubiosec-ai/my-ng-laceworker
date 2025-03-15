import os
import subprocess
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain_community.tools import ShellTool

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Function to execute shell commands safely
def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else f"Error: {result.stderr.strip()}"
    except Exception as e:
        return str(e)

# Function to sanitize filenames (for documentation lookup)
def sanitize_filename(name):
    import re
    name = re.sub(r'http[s]?://\S+', '', name)  # Remove URLs
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip('_')  # Replace invalid characters

# Function to retrieve documentation
def get_documentation(command, docs_dir='lacework_cli_docs'):
    command_file = sanitize_filename(command.replace(' ', '_')) + '.md'
    file_path = os.path.join(docs_dir, command_file)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        return f"Documentation for '{command}' not found."

# Function to execute Lacework command and retrieve documentation
def execute_lacework_command(command):
    doc = get_documentation(command)
    if "not found" in doc:
        return doc
    else:
        return run_shell_command(command)

# Initialize ShellTool for executing commands
shell_tool = ShellTool()

# Initialize OpenAI language model
llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

# Define tools for the agent
tools = [
    {
        'name': 'lacework_executor',
        'func': execute_lacework_command,
        'description': 'Executes Lacework CLI commands and retrieves documentation.'
    },
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
    uvicorn.run(app, host="0.0.0.0", port=8000)
