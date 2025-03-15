# Lacework CLI Agent with Vector Search

A FastAPI application that uses LangChain, FAISS vector store, and OpenAI to provide a natural language interface to the Lacework CLI.

## Overview

This application allows users to interact with the Lacework CLI using natural language commands. It uses:

- **FastAPI**: For the web API interface
- **LangChain**: For the agent framework that processes natural language
- **FAISS**: For efficient vector similarity search
- **OpenAI**: For language understanding, processing, and embeddings
- **Lacework CLI**: For executing Lacework commands

## How It Works

This agent uses a vector store approach to find relevant documentation:

1. **Combined Documentation**: All Lacework CLI documentation files are combined into a single `help.txt` file using the `combine_docs.py` script.

2. **Documentation Indexing**: The combined documentation file is loaded, split into chunks, and indexed in a FAISS vector store using OpenAI embeddings.

3. **Semantic Search**: When a user submits a query, the system performs a semantic search to find the most relevant documentation chunks.

4. **Command Generation**: The system uses the relevant documentation and the user's query to generate an appropriate Lacework CLI command.

5. **Command Execution**: The generated command can be executed directly through the agent.

This approach offers several advantages:
- More accurate matching of user intent to documentation
- Better handling of natural language queries
- Ability to find relevant information even when the query doesn't exactly match documentation keywords
- Improved context by having all documentation in a single file with cross-references

## Prerequisites

- Python 3.8+
- Lacework CLI installed and accessible in your PATH
- OpenAI API key
- Lacework account credentials (account name, API key, API secret)

## Installation

1. Clone the repository or download the source code

2. Install the required dependencies using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

3. Install the Lacework CLI if you haven't already (follow Lacework's official documentation)

## Configuration

### 1. OpenAI API Key

The application requires an OpenAI API key to function. You can provide this in two ways:

**Option 1**: Set it as an environment variable:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

**Option 2**: Create a `.env` file in the project directory:

1. Copy the example file:
```bash
cp .env.example .env
```

2. Edit the `.env` file and replace the placeholder with your actual OpenAI API key:
```
OPENAI_API_KEY=your-actual-openai-api-key-here
```

If you don't have an OpenAI API key, you can get one from the [OpenAI website](https://platform.openai.com/api-keys).

### 2. Lacework CLI Configuration

Configure the Lacework CLI with your account credentials:

```bash
lacework configure
```

This will prompt you for:
- Account name (your Lacework subdomain)
- API key
- API secret

You can obtain these credentials from your Lacework account settings.

## Running the Application

First, combine all the documentation files into a single help.txt file:

```bash
python combine_docs.py
```

This will create a help.txt file containing all the Lacework CLI documentation.

Then, start the application:

```bash
python agent_vs.py
```

The application will:
1. Load and index the combined documentation file (this may take a minute)
2. Automatically find an available port starting from 8080
3. Start a FastAPI server on the selected port
4. Display the URL where the service is running

Example output:
```
Loading documentation into vector store...
Documentation loaded successfully!
Starting server on port 8080
INFO:     Started server process [67270]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

## Testing the API

### Using curl

You can test the API using curl:

```bash
curl -X POST http://localhost:8080/execute/ \
  -H "Content-Type: application/json" \
  -d '{"command": "Show me how to list all alerts"}'
```

Replace `8080` with the actual port if different.

### Using the Swagger UI

FastAPI automatically generates interactive documentation:

1. Open your browser and navigate to `http://localhost:8080/docs`
2. Find the `/execute/` endpoint and click on it
3. Click "Try it out"
4. Enter a JSON payload with your command:
   ```json
   {
     "command": "Show me how to list all alerts"
   }
   ```
5. Click "Execute" and view the response

### Example Commands

- `"Show me recent alerts"`
- `"How do I list all Lacework agents?"`
- `"What's the command to show vulnerability information for containers?"`
- `"How can I configure Lacework?"`
- `"I need to create a new cloud account integration"`

## Troubleshooting

### Port Already in Use

If you see an error like "address already in use", the application will automatically try the next port up to 8090. If all ports are in use, you may need to manually free up a port or modify the code to use a different port range.

### API Key Issues

If you see authentication errors:

1. Verify your OpenAI API key is correct and has sufficient credits
2. Check that the environment variable or `.env` file is properly set

### Lacework CLI Errors

If you see Lacework CLI errors:

1. Ensure the Lacework CLI is properly installed and in your PATH
2. Verify your Lacework credentials are correctly configured
3. Run `lacework configure` to update your credentials if needed

### Vector Store Issues

If you encounter issues with the vector store:

1. Make sure the `help.txt` file exists (run `python combine_docs.py` to create it)
2. Ensure the `lacework_cli_docs` directory exists and contains documentation files
3. Check that you have the required dependencies installed (faiss-cpu, tiktoken)
4. Ensure your OpenAI API key has access to the embeddings API

## Differences from the Original Agent

This vector store-based agent differs from the original `agent_lacework.py` in several ways:

1. **Semantic Search**: Uses vector embeddings for semantic search rather than exact filename matching
2. **Command Generation**: Generates commands based on relevant documentation rather than just retrieving documentation
3. **Better Natural Language Understanding**: Can handle a wider range of natural language queries
4. **More Accurate Results**: Provides more relevant information by searching across all documentation content

## Performance Considerations

- The initial loading of documentation into the vector store may take some time, especially with a large number of documentation files
- Each query requires generating embeddings, which counts toward your OpenAI API usage
- For best performance, use specific queries that clearly state what you're trying to accomplish
