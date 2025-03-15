"""
Main module for Lacework Agent.
Provides the entry point for the application.
"""

import argparse
import asyncio
import logging
import sys

from .utils import setup_logging, check_openai_api_key
from .operations import update_vector_store, attach_files_to_vector_store
from .verification import verify_vector_store, verify_vector_store_simple
from .cleanup import delete_vector_store_and_files, retry_failed_files
from .agent import ask_prompt, run_agent, run_agent_with_sdk

# Check if OpenAI Agents SDK is available
try:
    from agents import Agent, Runner
    AGENTS_SDK_AVAILABLE = True
except ImportError:
    AGENTS_SDK_AVAILABLE = False

def main():
    """
    Main entry point for the application.
    
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    # Set up logging
    setup_logging()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Lacework Agent with Vector Store capabilities")
    parser.add_argument("--update", action="store_true", help="Update the vector store with documentation files and verify")
    parser.add_argument("--verify", action="store_true", help="Verify that all files have been uploaded to the vector store")
    parser.add_argument("--simple-verify", action="store_true", help="Simple verification of vector store files")
    parser.add_argument("--attach_files", action="store_true", help="Attach files one by one to the vector store and verify each")
    parser.add_argument("--delete", action="store_true", help="Delete the vector store, all its files, and related OpenAI files")
    parser.add_argument("--retry-failed", action="store_true", help="Retry uploading files that failed in the vector store")
    parser.add_argument("--prompt", type=str, help="Ask a question to the vector store and get a response")
    parser.add_argument("--agent", type=str, help="Run the agent to solve complex tasks and return bash commands")
    parser.add_argument("--agentsdk", type=str, help="Run the agent using the OpenAI Agents SDK")
    parser.add_argument("--web", action="store_true", help="Start the web interface")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to run the web server on (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8080, help="Port to run the web server on (default: 8080)")
    parser.add_argument("--debug", action="store_true", help="Run the web server in debug mode")
    
    args = parser.parse_args()
    
    # Check if any arguments were provided
    if len(sys.argv) == 1:
        parser.print_help()
        return 0
    
    # Check if OpenAI API key is set
    if not check_openai_api_key():
        return 1
    
    # Execute the requested operation
    try:
        if args.web:
            # Import web module here to avoid circular imports
            from .web import run_web_server
            print(f"Starting web server on http://{args.host}:{args.port}")
            print("Press Ctrl+C to stop the server")
            print("\nNote: If you're on macOS and port 5000 is in use by AirPlay Receiver,")
            print("you can disable it in System Preferences -> General -> AirDrop & Handoff,")
            print("or use a different port with --port option.")
            run_web_server(host=args.host, port=args.port, debug=args.debug)
        elif args.agentsdk:
            if AGENTS_SDK_AVAILABLE:
                asyncio.run(run_agent_with_sdk(args.agentsdk))
            else:
                print("Error: OpenAI Agents SDK is not installed. Please install it with: pip install openai-agents")
                return 1
        elif args.agent:
            run_agent(args.agent)
        elif args.prompt:
            ask_prompt(args.prompt)
        elif args.update:
            update_vector_store()
        elif args.verify:
            verify_vector_store()
        elif args.simple_verify:
            verify_vector_store_simple()
        elif args.attach_files:
            attach_files_to_vector_store()
        elif args.delete:
            delete_vector_store_and_files()
        elif args.retry_failed:
            retry_failed_files()
        
        return 0
    
    except Exception as e:
        logging.exception(f"Error in main: {str(e)}")
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
