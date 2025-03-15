"""
Cleanup module for Lacework Agent.
Handles cleanup operations for vector stores and files.
"""

import os
import logging
import time
from dotenv import load_dotenv
from openai import OpenAI

from .config import load_config, save_config
from .file_operations import get_all_markdown_files, get_file_basenames
from .verification import verify_vector_store

def delete_vector_store_and_files():
    """
    Delete the vector store, all its files, and related OpenAI files.
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return False
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    vector_store_exists = False
    
    # Check if vector store ID exists
    if config["vector_store_id"]:
        vector_store_id = config["vector_store_id"]
        vector_store_exists = True
        logging.info(f"Preparing to delete vector store with ID: {vector_store_id}")
        print(f"Preparing to delete vector store with ID: {vector_store_id}")
    else:
        logging.info("No vector store ID found in config file")
        print("No vector store ID found in config file")
        print("Skipping vector store deletion, but will still clean up OpenAI files")
    
    try:
        if vector_store_exists:
            # Step 1: Get all files in the vector store with pagination
            logging.info("Retrieving all files from the vector store...")
            print("\nStep 1: Retrieving all files from the vector store...")
            all_files_data = []
            has_more = True
            after = None
            page = 1
            
            try:
                while has_more:
                    logging.info(f"Fetching page {page} of vector store files...")
                    print(f"Fetching page {page} of vector store files...")
                    
                    # Set up pagination parameters
                    params = {
                        "vector_store_id": vector_store_id,
                        "limit": 100  # Maximum allowed limit
                    }
                    
                    # Add 'after' parameter for pagination if we have a cursor
                    if after:
                        params["after"] = after
                    
                    # Get the current page of files
                    vector_store_files = client.vector_stores.files.list(**params)
                    
                    # Add files to our collection
                    all_files_data.extend(vector_store_files.data)
                    
                    # Check if there are more pages
                    has_more = vector_store_files.has_more if hasattr(vector_store_files, 'has_more') else False
                    
                    # Get the cursor for the next page
                    if has_more and hasattr(vector_store_files, 'last_id'):
                        after = vector_store_files.last_id
                    
                    page += 1
                
                logging.info(f"Found {len(all_files_data)} files in the vector store")
                print(f"Found {len(all_files_data)} files in the vector store")
                
                # Step 2: Delete all files from the vector store
                logging.info("Deleting files from the vector store...")
                print("\nStep 2: Deleting files from the vector store...")
                deleted_vs_files = 0
                
                for file in all_files_data:
                    try:
                        logging.info(f"Deleting file {file.id} from vector store...")
                        print(f"Deleting file {file.id} from vector store...")
                        
                        deleted = client.vector_stores.files.delete(
                            vector_store_id=vector_store_id,
                            file_id=file.id
                        )
                        
                        if deleted.deleted:
                            deleted_vs_files += 1
                            logging.info(f"Successfully deleted file {file.id} from vector store")
                            print(f"✅ Successfully deleted file {file.id} from vector store")
                        else:
                            logging.warning(f"Failed to delete file {file.id} from vector store")
                            print(f"⚠️ Failed to delete file {file.id} from vector store")
                    except Exception as e:
                        logging.error(f"Error deleting file {file.id} from vector store: {str(e)}")
                        print(f"Error deleting file {file.id} from vector store: {str(e)}")
                
                logging.info(f"Deleted {deleted_vs_files} out of {len(all_files_data)} files from the vector store")
                print(f"Deleted {deleted_vs_files} out of {len(all_files_data)} files from the vector store")
                
                # Step 3: Delete the vector store
                logging.info("Deleting the vector store...")
                print("\nStep 3: Deleting the vector store...")
                try:
                    deleted_vs = client.vector_stores.delete(vector_store_id=vector_store_id)
                    if deleted_vs.deleted:
                        logging.info(f"Successfully deleted vector store {vector_store_id}")
                        print(f"✅ Successfully deleted vector store {vector_store_id}")
                    else:
                        logging.warning(f"Failed to delete vector store {vector_store_id}")
                        print(f"⚠️ Failed to delete vector store {vector_store_id}")
                except Exception as e:
                    logging.error(f"Error deleting vector store: {str(e)}")
                    print(f"Error deleting vector store: {str(e)}")
                    print("The vector store may no longer exist. Continuing with cleanup...")
            except Exception as e:
                logging.error(f"Error accessing vector store: {str(e)}")
                print(f"Error accessing vector store: {str(e)}")
                print("The vector store may no longer exist. Continuing with cleanup...")
        
        # Step 4: Delete all OpenAI files that start with "lacework_"
        logging.info("Deleting OpenAI files that start with 'lacework_'...")
        print("\nStep 4: Deleting OpenAI files that start with 'lacework_'...")
        all_openai_files = client.files.list()
        lacework_files = [file for file in all_openai_files.data if file.filename.startswith("lacework_")]
        
        logging.info(f"Found {len(lacework_files)} OpenAI files that start with 'lacework_'")
        print(f"Found {len(lacework_files)} OpenAI files that start with 'lacework_'")
        deleted_openai_files = 0
        
        for file in lacework_files:
            try:
                logging.info(f"Deleting OpenAI file {file.id} ({file.filename})...")
                print(f"Deleting OpenAI file {file.id} ({file.filename})...")
                
                deleted = client.files.delete(file_id=file.id)
                if deleted.deleted:
                    deleted_openai_files += 1
                    logging.info(f"Successfully deleted OpenAI file {file.id}")
                    print(f"✅ Successfully deleted OpenAI file {file.id}")
                else:
                    logging.warning(f"Failed to delete OpenAI file {file.id}")
                    print(f"⚠️ Failed to delete OpenAI file {file.id}")
            except Exception as e:
                logging.error(f"Error deleting OpenAI file {file.id}: {str(e)}")
                print(f"Error deleting OpenAI file {file.id}: {str(e)}")
        
        logging.info(f"Deleted {deleted_openai_files} out of {len(lacework_files)} OpenAI files")
        print(f"Deleted {deleted_openai_files} out of {len(lacework_files)} OpenAI files")
        
        # Step 5: Remove the vector store ID from the config file
        if config["vector_store_id"]:
            logging.info("Removing vector store ID from config file...")
            print("\nStep 5: Removing vector store ID from config file...")
            config["vector_store_id"] = None
            save_config(config)
            logging.info("Successfully removed vector store ID from config file")
            print(f"✅ Successfully removed vector store ID from config file")
        
        logging.info("Cleanup complete!")
        print("\nCleanup complete!")
        return True
        
    except Exception as e:
        logging.exception(f"Error during cleanup: {str(e)}")
        print(f"Error during cleanup: {str(e)}")
        return False

def retry_failed_files():
    """
    Retry uploading files that failed in the vector store.
    
    Returns:
        tuple: (int, int) - Number of successful retries and total retries
    """
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return 0, 0
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        logging.error("No vector store ID found in config file")
        print("Error: No vector store ID found in config file")
        print("Please run with --update first to create a vector store")
        return 0, 0
    
    vector_store_id = config["vector_store_id"]
    logging.info(f"Checking for failed files in vector store with ID: {vector_store_id}")
    print(f"Checking for failed files in vector store with ID: {vector_store_id}")
    
    # First, verify the vector store to identify failed files
    success, failed_files = verify_vector_store(client, vector_store_id)
    
    if not failed_files:
        logging.info("No failed files found to retry")
        print("No failed files found to retry")
        return 0, 0
    
    logging.info(f"Found {len(failed_files)} failed files to retry")
    print(f"\nFound {len(failed_files)} failed files to retry")
    
    # Get all local files
    local_files = get_all_markdown_files()
    local_filenames = {os.path.basename(f): f for f in local_files}
    
    # Get all OpenAI files to match with failed vector store files
    all_openai_files = client.files.list()
    openai_files = {file.id: file for file in all_openai_files.data if file.purpose == "assistants"}
    
    # Track statistics
    retry_count = 0
    success_count = 0
    
    # Process each failed file
    for failed_file in failed_files:
        retry_count += 1
        file_id = failed_file.id
        
        logging.info(f"Processing failed file {file_id}")
        print(f"\nProcessing failed file {file_id}")
        
        # Try to find the corresponding OpenAI file
        if file_id in openai_files:
            openai_file = openai_files[file_id]
            filename = openai_file.filename
            
            # Check if we have the local file
            if filename in local_filenames:
                local_path = local_filenames[filename]
                
                # First, remove the file from the vector store
                try:
                    logging.info(f"Removing file {file_id} from vector store")
                    print(f"Removing file {file_id} from vector store...")
                    
                    deleted = client.vector_stores.files.delete(
                        vector_store_id=vector_store_id,
                        file_id=file_id
                    )
                    
                    if deleted.deleted:
                        logging.info(f"Successfully removed file {file_id} from vector store")
                        print(f"✅ Successfully removed file {file_id} from vector store")
                        
                        # Wait a moment before re-uploading
                        time.sleep(1)
                        
                        # Now re-upload the file
                        logging.info(f"Re-uploading file {filename}")
                        print(f"Re-uploading file {filename}...")
                        
                        from .file_operations import attach_file_to_vector_store
                        if attach_file_to_vector_store(client, vector_store_id, local_path):
                            success_count += 1
                            logging.info(f"Successfully re-uploaded file {filename}")
                            print(f"✅ Successfully re-uploaded file {filename}")
                        else:
                            logging.error(f"Failed to re-upload file {filename}")
                            print(f"❌ Failed to re-upload file {filename}")
                    else:
                        logging.error(f"Failed to remove file {file_id} from vector store")
                        print(f"❌ Failed to remove file {file_id} from vector store")
                except Exception as e:
                    logging.exception(f"Error processing file {file_id}: {str(e)}")
                    print(f"Error processing file {file_id}: {str(e)}")
            else:
                logging.warning(f"Local file not found for {filename}")
                print(f"⚠️ Local file not found for {filename}")
        else:
            logging.warning(f"OpenAI file not found for vector store file {file_id}")
            print(f"⚠️ OpenAI file not found for vector store file {file_id}")
        
        # Add a separator between files
        print("-" * 40)
    
    # Print summary
    logging.info(f"Retry Summary: {success_count} of {retry_count} files successfully re-uploaded")
    print(f"\nRetry Summary:")
    print(f"- Total files processed: {retry_count}")
    print(f"- Successfully re-uploaded: {success_count}")
    print(f"- Failed to re-upload: {retry_count - success_count}")
    
    # Verify the final state
    print("\nVerifying final state of vector store...")
    verify_vector_store(client, vector_store_id)
    
    return success_count, retry_count
