"""
Operations module for Lacework Agent.
Handles the main operations for the agent.
"""

import os
import logging
import time
from dotenv import load_dotenv
from openai import OpenAI

from .config import load_config, save_config
from .vector_store import get_or_create_vector_store, upload_docs_to_vector_store
from .file_operations import attach_file_to_vector_store, get_all_markdown_files, get_lacework_files, get_file_basenames
from .verification import verify_vector_store
from .utils import check_openai_api_key

def update_vector_store():
    """
    Main function to update the vector store (manage file uploads and prevent duplicates).
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not check_openai_api_key():
        return False
    
    # Initialize OpenAI client
    client = OpenAI()
    
    try:
        # Get or create vector store
        vector_store_id = get_or_create_vector_store(client)
        
        # Get all local files
        local_files = get_all_markdown_files()
        local_filenames = get_file_basenames(local_files)
        
        if not local_files:
            logging.warning("No markdown files found in docs directory")
            print("No markdown files found in docs directory")
            return False
        
        logging.info(f"Found {len(local_files)} local markdown files")
        print(f"Found {len(local_files)} local markdown files")
        
        # Get all OpenAI files to check for duplicates
        all_openai_files = client.files.list()
        uploaded_filenames = [file.filename for file in all_openai_files.data if file.purpose == "assistants"]
        
        # Find files that haven't been uploaded yet
        new_files = []
        for file_path in local_files:
            filename = os.path.basename(file_path)
            if filename not in uploaded_filenames:
                new_files.append(file_path)
        
        if not new_files:
            logging.info("All files are already uploaded to OpenAI")
            print("\nAll files are already uploaded to OpenAI")
        else:
            logging.info(f"Found {len(new_files)} new files to upload")
            print(f"\nFound {len(new_files)} new files to upload")
            
            # Process each new file one by one
            successful_files = 0
            failed_files = 0
            
            for file_path in new_files:
                filename = os.path.basename(file_path)
                logging.info(f"Uploading new file: {filename}")
                print(f"Uploading new file: {filename}")
                
                if attach_file_to_vector_store(client, vector_store_id, file_path):
                    successful_files += 1
                else:
                    failed_files += 1
                
                # Add a small separator between files
                print("-" * 40)
            
            # Print summary
            logging.info(f"Upload Summary: {successful_files} of {len(new_files)} files successfully uploaded")
            print("\nUpload Summary:")
            print(f"- Total new files processed: {len(new_files)}")
            print(f"- Successfully uploaded: {successful_files}")
            print(f"- Failed to upload: {failed_files}")
        
        # Verify the final state
        print("\nVerifying vector store status...")
        verify_vector_store(client, vector_store_id)
        
        return True
    
    except Exception as e:
        logging.exception(f"Error updating vector store: {str(e)}")
        print(f"Error updating vector store: {str(e)}")
        return False

def attach_files_to_vector_store():
    """
    Attach files one by one to the vector store.
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not check_openai_api_key():
        return False
    
    # Initialize OpenAI client
    client = OpenAI()
    
    try:
        # Get or create vector store
        vector_store_id = get_or_create_vector_store(client)
        
        # Get all markdown files in the docs directory that start with "lacework"
        file_paths = get_lacework_files()
        
        if not file_paths:
            logging.warning("No lacework markdown files found in docs directory")
            print("No lacework markdown files found in docs directory")
            return False
        
        logging.info(f"Found {len(file_paths)} lacework markdown files to attach")
        print(f"Found {len(file_paths)} lacework markdown files to attach")
        
        # Get all files in the vector store
        logging.info("Checking for existing files in vector store...")
        print("Checking for existing files in vector store...")
        
        vector_store_files = []
        has_more = True
        after = None
        
        while has_more:
            params = {
                "vector_store_id": vector_store_id,
                "limit": 100
            }
            
            if after:
                params["after"] = after
            
            vs_files_response = client.vector_stores.files.list(**params)
            vector_store_files.extend(vs_files_response.data)
            
            has_more = vs_files_response.has_more if hasattr(vs_files_response, 'has_more') else False
            if has_more and hasattr(vs_files_response, 'last_id'):
                after = vs_files_response.last_id
        
        # Get IDs of files already in the vector store
        vector_store_file_ids = [file.id for file in vector_store_files]
        logging.info(f"Found {len(vector_store_file_ids)} files already in vector store")
        print(f"Found {len(vector_store_file_ids)} files already in vector store")
        
        # Get all OpenAI files
        all_openai_files = client.files.list()
        openai_files = {file.filename: file for file in all_openai_files.data if file.purpose == "assistants"}
        
        logging.info(f"Found {len(openai_files)} files already uploaded to OpenAI")
        print(f"Found {len(openai_files)} files already uploaded to OpenAI")
        
        # Process each lacework file
        successful_uploads = 0
        successful_attachments = 0
        failed_files = 0
        
        for file_path in file_paths:
            filename = os.path.basename(file_path)
            logging.info(f"Processing file: {filename}")
            print(f"\nProcessing file: {filename}")
            
            # Check if file is already uploaded to OpenAI
            if filename in openai_files:
                openai_file = openai_files[filename]
                file_id = openai_file.id
                
                logging.info(f"File already uploaded to OpenAI with ID: {file_id}")
                print(f"File already uploaded to OpenAI with ID: {file_id}")
                
                # Check if file is already in the vector store
                if file_id in vector_store_file_ids:
                    logging.info("File already attached to vector store")
                    print("File already attached to vector store")
                    continue
                
                # Attach existing file to vector store
                logging.info(f"Attaching existing file to vector store: {file_id}")
                print("Attaching existing file to vector store...")
                
                try:
                    # Attach the file to the vector store
                    vector_store_file = client.vector_stores.files.create(
                        vector_store_id=vector_store_id,
                        file_id=file_id
                    )
                    
                    # Verify the attachment
                    time.sleep(1)  # Wait a moment for processing
                    
                    file_status = client.vector_stores.files.retrieve(
                        vector_store_id=vector_store_id,
                        file_id=file_id
                    )
                    
                    status = file_status.status if hasattr(file_status, 'status') else "unknown"
                    
                    if status in ["completed", "in_progress"]:
                        logging.info(f"Successfully attached existing file: {filename}")
                        print(f"✅ Successfully attached existing file: {filename}")
                        successful_attachments += 1
                    else:
                        logging.error(f"Failed to attach existing file: {filename}, status: {status}")
                        print(f"❌ Failed to attach existing file: {filename}, status: {status}")
                        failed_files += 1
                        
                        if hasattr(file_status, 'last_error') and file_status.last_error:
                            logging.error(f"Error details: {file_status.last_error}")
                            print(f"  Error details: {file_status.last_error}")
                    
                except Exception as e:
                    logging.exception(f"Error attaching existing file: {str(e)}")
                    print(f"Error attaching existing file: {str(e)}")
                    failed_files += 1
            else:
                # Upload and attach new file
                logging.info(f"Uploading new file: {filename}")
                print(f"Uploading new file: {filename}")
                
                if attach_file_to_vector_store(client, vector_store_id, file_path):
                    successful_uploads += 1
                else:
                    failed_files += 1
            
            # Add a small separator between files
            print("-" * 40)
            
            # Add a small delay between operations to avoid rate limiting
            time.sleep(1)
        
        # Print summary
        logging.info(f"Attachment Summary: {successful_uploads} new uploads, {successful_attachments} existing files attached, {failed_files} failures")
        print("\nAttachment Summary:")
        print(f"- New files uploaded and attached: {successful_uploads}")
        print(f"- Existing files attached to vector store: {successful_attachments}")
        print(f"- Failed operations: {failed_files}")
        
        # Verify the final state
        print("\nVerifying final state of vector store...")
        verify_vector_store(client, vector_store_id)
        
        return True
    
    except Exception as e:
        logging.exception(f"Error attaching files to vector store: {str(e)}")
        print(f"Error attaching files to vector store: {str(e)}")
        return False
