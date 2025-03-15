"""
File operations module for Lacework Agent.
Handles file attachments and operations with the vector store.
"""

import os
import glob
import logging
import time
from .config import DOCS_DIR

def attach_file_to_vector_store(client, vector_store_id, file_path):
    """
    Attach a single file to the vector store and verify completion.
    
    Args:
        client (OpenAI): OpenAI client instance
        vector_store_id (str): ID of the vector store
        file_path (str): Path to the file to attach
        
    Returns:
        bool: True if successful, False otherwise
    """
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        print(f"Error: File not found: {file_path}")
        return False
    
    filename = os.path.basename(file_path)
    logging.info(f"Attaching file: {filename}")
    print(f"Attaching file: {filename}")
    
    try:
        # Step 1: Upload the file to OpenAI
        logging.info(f"Step 1: Uploading file to OpenAI: {filename}")
        print(f"Step 1: Uploading file to OpenAI...")
        
        with open(file_path, "rb") as file_stream:
            uploaded_file = client.files.create(
                file=file_stream,
                purpose="assistants"
            )
        
        file_id = uploaded_file.id
        logging.info(f"File uploaded with ID: {file_id}")
        print(f"File uploaded with ID: {file_id}")
        
        # Step 2: Attach the file to the vector store
        logging.info(f"Step 2: Attaching file to vector store: {file_id}")
        print(f"Step 2: Attaching file to vector store...")
        
        # Wait a moment before attaching to ensure the file is processed
        time.sleep(1)
        
        vector_store_file = client.vector_stores.files.create(
            vector_store_id=vector_store_id,
            file_id=file_id
        )
        
        # Step 3: Verify the file was attached successfully
        logging.info(f"Verifying file attachment status...")
        print(f"Verifying file attachment status...")
        
        # Wait a moment to allow processing
        time.sleep(1)
        
        # Check the status of the file in the vector store
        file_status = client.vector_stores.files.retrieve(
            vector_store_id=vector_store_id,
            file_id=file_id
        )
        
        status = file_status.status if hasattr(file_status, 'status') else "unknown"
        logging.info(f"File attachment status: {status}")
        print(f"File attachment status: {status}")
        
        if status == "completed":
            logging.info(f"File successfully attached: {filename}")
            print(f"✅ File successfully attached: {filename}")
            return True
        elif status == "in_progress":
            logging.info(f"File attachment in progress: {filename}")
            print(f"⏳ File attachment in progress: {filename}")
            print(f"  The file will continue processing in the background.")
            return True
        else:
            logging.error(f"File attachment has issues: {status}")
            print(f"⚠️ File attachment has issues: {status}")
            
            if hasattr(file_status, 'last_error') and file_status.last_error:
                logging.error(f"Error details: {file_status.last_error}")
                print(f"  Error details: {file_status.last_error}")
            
            return False
    
    except Exception as e:
        logging.exception(f"Error attaching file: {str(e)}")
        print(f"Error attaching file: {str(e)}")
        return False

def get_lacework_files():
    """
    Get all markdown files in the docs directory that start with "lacework".
    
    Returns:
        list: List of file paths
    """
    file_paths = glob.glob(os.path.join(DOCS_DIR, "lacework*.md"))
    return file_paths

def get_all_markdown_files():
    """
    Get all markdown files in the docs directory.
    
    Returns:
        list: List of file paths
    """
    file_paths = glob.glob(os.path.join(DOCS_DIR, "*.md"))
    return file_paths

def get_file_basenames(file_paths):
    """
    Get the basenames of a list of file paths.
    
    Args:
        file_paths (list): List of file paths
        
    Returns:
        list: List of file basenames
    """
    return [os.path.basename(f) for f in file_paths]
