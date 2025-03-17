# Lacework Agent with Vector Store

A modular Python application for interacting with Lacework CLI documentation via OpenAI's vector store capabilities.

## Project Structure

The project follows a modular structure for better organization and maintainability:

```
lacework_agent_new/
├── lacework_agent_new.py  # Main entry point
├── src/
│   ├── __init__.py        # Package initialization
│   ├── agent.py           # Agent operations (ask_prompt, run_agent)
│   ├── cleanup.py         # Cleanup operations (delete_vector_store, retry_failed_files)
│   ├── config.py          # Configuration handling (load_config, save_config)
│   ├── file_operations.py # File operations (attach_file_to_vector_store)
│   ├── main.py            # Main module with argument parsing
│   ├── operations.py      # Main operations (update_vector_store, attach_files)
│   ├── utils.py           # Utility functions (save_trace, vector_search)
│   ├── vector_store.py    # Vector store operations (create_vector_store)
│   └── web.py             # Web interface using Flask
├── templates/             # HTML templates for web interface
│   └── index.html         # Main page template
├── static/                # Static files for web interface
│   ├── css/               # CSS stylesheets
│   │   └── style.css      # Custom styles
│   └── js/                # JavaScript files
│       └── script.js      # Client-side functionality
├── logs/                  # Log files (created at runtime)
└── traces/                # Trace files (created at runtime)
```

## Features

- Create and manage vector stores for Lacework CLI documentation
- Upload and attach files to vector stores
- Verify vector store status and file attachments
- Retry failed file uploads
- Ask questions to the vector store and get responses
- Run an agent to solve complex tasks and return bash commands
- Support for OpenAI Agents SDK (if installed)
- Web interface for easy interaction with the agent

## Requirements

- Python 3.8+
- OpenAI API key
- Required Python packages:
  - openai
  - python-dotenv
  - flask
  - (Optional) openai-agents

## Installation

1. Clone the repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### Command Line Interface

The application provides various command-line options:

```
# Show help
python lacework_agent_new.py --help

# Update the vector store with documentation files
python lacework_agent_new.py --update

# Verify that all files have been uploaded to the vector store
python lacework_agent_new.py --verify

# Simple verification of vector store files
python lacework_agent_new.py --simple-verify

# Attach files one by one to the vector store
python lacework_agent_new.py --attach_files

# Delete the vector store and related files
python lacework_agent_new.py --delete

# Retry uploading files that failed in the vector store
python lacework_agent_new.py --retry-failed

# Ask a question to the vector store
python lacework_agent_new.py --prompt "How do I list Lacework agents?"

# Run the agent to solve complex tasks
python lacework_agent_new.py --agent "Show me how to configure Lacework for AWS"

# Run the agent using the OpenAI Agents SDK (if installed)
python lacework_agent_new.py --agentsdk "Show me how to configure Lacework for AWS"
```

### Web Interface

The application also provides a web interface for easier interaction:

```
# Start the web interface on default port (8080)
python lacework_agent_new.py --web

# Start the web interface on a specific host and port
python lacework_agent_new.py --web --host 127.0.0.1 --port 9000

# Start the web interface in debug mode
python lacework_agent_new.py --web --debug
```

Once the web server is running, open your browser and navigate to the URL shown in the console (e.g., http://127.0.0.1:8080). The web interface provides:

- A dropdown to select the mode (prompt, agent, agentsdk)
- A text box to enter your questions or tasks
- A section to display the answers or results

### Note for macOS Users

On macOS, port 5000 is often used by the AirPlay Receiver service. If you encounter an "Address already in use" error when starting the web interface, you have two options:

1. Use a different port:
   ```
   python lacework_agent_new.py --web --port 9000
   ```

2. Disable the AirPlay Receiver service:
   - Go to System Preferences -> General -> AirDrop & Handoff
   - Disable the 'AirPlay Receiver' service

## Logs and Traces

- Log files are stored in the `logs/` directory with timestamps
- Trace files for agent runs are stored in the `traces/` directory with timestamps

## License

This project is licensed under the MIT License - see the LICENSE file for details.
