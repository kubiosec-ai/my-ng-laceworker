"""
Vector store operations module for Lacework Agent.
Handles creating and managing vector stores.
"""

import os
import glob
import logging
import time
from openai import OpenAI
from .config import DOCS_DIR, load_config, save_config

def create_vector_store(client, name="Lacework CLI Documentation"):
    """
    Create a new vector store and return its ID.
    
    Args:
        client (OpenAI): OpenAI client instance
        name (str): Name for the vector store
        
    Returns:
        object: Vector store object
    """
    logging.info(f"Creating vector store: {name}")
    print(f"Creating vector store: {name}")
    
    try:
        vector_store = client.vector_stores.create(name=name)
        logging.info(f"Vector store created with ID: {vector_store.id}")
        print(f"Vector store created with ID: {vector_store.id}")
        return vector_store
    except Exception as e:
        logging.error(f"Error creating vector store: {str(e)}")
        print(f"Error creating vector store: {str(e)}")
        raise

def upload_docs_to_vector_store(client, vector_store_id):
    """
    Upload all markdown files from lacework_cli_docs to the vector store.
    
    Args:
        client (OpenAI): OpenAI client instance
        vector_store_id (str): ID of the vector store
        
    Returns:
        object: File batch object or None if failed
    """
    # Get all markdown files in the docs directory
    file_paths = glob.glob(os.path.join(DOCS_DIR, "*.md"))
    
    if not file_paths:
        logging.warning(f"No markdown files found in {DOCS_DIR}")
        print(f"No markdown files found in {DOCS_DIR}")
        return None
    
    logging.info(f"Found {len(file_paths)} markdown files to upload")
    print(f"Found {len(file_paths)} markdown files to upload")
    
    # Open file streams for all files
    file_streams = [open(path, "rb") for path in file_paths]
    
    try:
        # Upload files to vector store
        logging.info("Uploading files to vector store...")
        print("Uploading files to vector store...")
        
        file_batch = client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id,
            files=file_streams
        )
        
        # Print status and file counts
        logging.info(f"Upload status: {file_batch.status}")
        print(f"Upload status: {file_batch.status}")
        
        if hasattr(file_batch, 'file_counts'):
            logging.info(f"File counts: {file_batch.file_counts}")
            print(f"File counts: {file_batch.file_counts}")
        
        return file_batch
    except Exception as e:
        logging.error(f"Error uploading files to vector store: {str(e)}")
        print(f"Error uploading files to vector store: {str(e)}")
        return None
    finally:
        # Close all file streams
        for stream in file_streams:
            stream.close()

def get_or_create_vector_store(client):
    """
    Get existing vector store or create a new one.
    
    Args:
        client (OpenAI): OpenAI client instance
        
    Returns:
        str: Vector store ID
    """
    # Load existing configuration
    config = load_config()
    
    # Check if vector store already exists
    if config["vector_store_id"]:
        try:
            # Verify the vector store exists by making a simple API call
            client.vector_stores.files.list(
                vector_store_id=config["vector_store_id"],
                limit=1
            )
            
            logging.info(f"Using existing vector store with ID: {config['vector_store_id']}")
            print(f"Using existing vector store with ID: {config['vector_store_id']}")
            return config["vector_store_id"]
        except Exception as e:
            logging.warning(f"Vector store with ID {config['vector_store_id']} not found: {str(e)}")
            print(f"Vector store with ID {config['vector_store_id']} not found.")
            print("Creating a new vector store...")
    else:
        logging.info("No vector store ID found in config. Creating a new vector store.")
        print("No vector store ID found in config. Creating a new vector store...")
    
    # Create new vector store
    vector_store = create_vector_store(client)
    vector_store_id = vector_store.id
    
    # Save vector store ID to config
    config["vector_store_id"] = vector_store_id
    save_config(config)
    logging.info(f"Saved vector store ID {vector_store_id} to config")
    print(f"Saved vector store ID to config")
    
    return vector_store_id
