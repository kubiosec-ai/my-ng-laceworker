"""
Utility module for Lacework Agent.
Provides utility functions for the agent.
"""

import os
import json
import logging
from datetime import datetime

# Tracing configuration
TRACE_DIR = "traces"
os.makedirs(TRACE_DIR, exist_ok=True)

def save_trace(trace_data, trace_id=None):
    """
    Save trace data to a JSON file.
    
    Args:
        trace_data (dict): The trace data to save
        trace_id (str, optional): The ID for the trace. If None, a new ID will be generated.
        
    Returns:
        str: The path to the saved trace file
    """
    if trace_id is None:
        trace_id = f"trace_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    trace_file = os.path.join(TRACE_DIR, f"{trace_id}.json")
    
    try:
        with open(trace_file, 'w') as f:
            json.dump(trace_data, f, indent=2)
        
        logging.info(f"Trace saved to {trace_file}")
        return trace_file
    except Exception as e:
        logging.error(f"Error saving trace: {str(e)}")
        print(f"Error saving trace: {str(e)}")
        return None

def vector_search(client, vector_store_id, query):
    """
    Search the vector store for relevant information.
    
    Args:
        client (OpenAI): OpenAI client instance
        vector_store_id (str): ID of the vector store
        query (str): The query to search for
        
    Returns:
        str: The search results
    """
    try:
        logging.info(f"Searching vector store for: {query}")
        print(f"Searching vector store for: {query}")
        
        # Use the OpenAI API to search the vector store
        response = client.responses.create(
            model="gpt-4o",
            input=f"Find information relevant to this query: {query}. Return only the most relevant information from the Lacework CLI documentation.",
            tools=[{
                "type": "file_search",
                "vector_store_ids": [vector_store_id]
            }]
        )
        
        # Extract relevant information from the response
        result = ""
        if hasattr(response, 'output') and response.output:
            for output_item in response.output:
                if hasattr(output_item, 'type') and output_item.type == 'message':
                    if hasattr(output_item, 'content') and output_item.content:
                        for content_item in output_item.content:
                            if hasattr(content_item, 'text'):
                                result += content_item.text + "\n"
        
        logging.info(f"Vector search found: {result[:100]}...")
        print(f"Vector search found relevant information")
        
        return result
    except Exception as e:
        error_msg = f"Error in vector search: {str(e)}"
        logging.exception(error_msg)
        print(error_msg)
        return f"Error searching vector store: {str(e)}"

def setup_logging(log_dir="logs"):
    """
    Set up logging for the application.
    
    Args:
        log_dir (str): Directory to store log files
        
    Returns:
        str: Path to the log file
    """
    # Create log directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)
    
    # Create log filename with timestamp
    log_filename = os.path.join(log_dir, f"lacework_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    
    logging.info(f"Logging initialized. Log file: {log_filename}")
    return log_filename

def check_openai_api_key():
    """
    Check if the OpenAI API key is set in the environment.
    
    Returns:
        bool: True if the API key is set, False otherwise
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return False
    return True
