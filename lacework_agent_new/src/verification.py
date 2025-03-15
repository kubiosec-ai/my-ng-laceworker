"""
Verification module for Lacework Agent.
Handles verification of vector store files and status.
"""

import os
import logging
import json
from dotenv import load_dotenv
from openai import OpenAI

from .config import load_config, DOCS_DIR
from .file_operations import get_all_markdown_files, get_file_basenames

def verify_vector_store(client=None, vector_store_id=None):
    """
    Verify that all files have been uploaded to the vector store.
    
    Args:
        client (OpenAI, optional): OpenAI client instance. If None, a new one will be created.
        vector_store_id (str, optional): ID of the vector store. If None, it will be loaded from config.
        
    Returns:
        tuple: (bool, list) - Success status and list of failed files
    """
    # If client is not provided, initialize it
    if client is None:
        # Load environment variables (for OPENAI_API_KEY)
        load_dotenv()
        
        # Check if OPENAI_API_KEY is set
        if not os.getenv("OPENAI_API_KEY"):
            logging.error("OPENAI_API_KEY environment variable is not set")
            print("Error: OPENAI_API_KEY environment variable is not set")
            print("Please set it in your .env file or environment")
            return False, []
        
        # Initialize OpenAI client
        client = OpenAI()
    
    # If vector_store_id is not provided, load it from config
    if vector_store_id is None:
        # Load existing configuration
        config = load_config()
        
        # Check if vector store ID exists
        if not config["vector_store_id"]:
            logging.error("No vector store ID found in config file")
            print("Error: No vector store ID found in config file")
            print("Please run with --update first to create a vector store")
            return False, []
        
        vector_store_id = config["vector_store_id"]
    
    logging.info(f"Verifying vector store with ID: {vector_store_id}")
    print(f"Verifying vector store with ID: {vector_store_id}")
    
    try:
        # Get all files in the vector store with pagination
        logging.info("Fetching files in the vector store...")
        print("Fetching files in the vector store...")
        all_files_data = []
        has_more = True
        after = None
        page = 1
        
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
        
        # Get all markdown files in the docs directory
        local_files = get_all_markdown_files()
        local_filenames = get_file_basenames(local_files)
        
        # Print summary
        logging.info(f"Summary: Vector store ID: {vector_store_id}, Files in vector store: {len(all_files_data)}, Local markdown files: {len(local_files)}")
        print(f"\nSummary:")
        print(f"- Vector store ID: {vector_store_id}")
        print(f"- Files in vector store: {len(all_files_data)}")
        print(f"- Local markdown files: {len(local_files)}")
        
        # Check if all files are uploaded
        if len(all_files_data) == len(local_files):
            logging.info("All files appear to be uploaded to the vector store")
            print("\n✅ All files appear to be uploaded to the vector store")
        else:
            logging.warning(f"Mismatch: {len(local_files)} local files, but {len(all_files_data)} files in vector store")
            print(f"\n⚠️ Mismatch: {len(local_files)} local files, but {len(all_files_data)} files in vector store")
            
            # Get all OpenAI files to check filenames
            all_openai_files = client.files.list()
            uploaded_filenames = [file.filename for file in all_openai_files.data if file.purpose == "assistants"]
            
            # Find missing files
            missing_files = set(local_filenames) - set(uploaded_filenames)
            if missing_files:
                logging.warning(f"Missing files: {missing_files}")
                print(f"\nMissing files (first 10):")
                for filename in list(missing_files)[:10]:
                    print(f"- {filename}")
                if len(missing_files) > 10:
                    print(f"  ... and {len(missing_files) - 10} more")
        
        # List all OpenAI files for reference (first 10 only)
        print("\nAll OpenAI files (first 10):")
        all_openai_files = client.files.list()
        for file in all_openai_files.data[:10]:
            print(f"- {file.id}: {file.filename} ({file.bytes} bytes, purpose: {file.purpose})")
        if len(all_openai_files.data) > 10:
            print(f"  ... and {len(all_openai_files.data) - 10} more")
        
        # List files in the vector store with status (first 10 only)
        print("\nFiles in this vector store (first 10):")
        file_statuses = {}
        failed_files = []
        
        for file in all_files_data:
            status_info = ""
            if hasattr(file, 'status'):
                status = file.status
                status_info = f", status: {status}"
                file_statuses[status] = file_statuses.get(status, 0) + 1
                
                # Collect failed files
                if status == "failed":
                    failed_files.append(file)
            
            # Log file details
            if hasattr(file, 'last_error') and file.last_error:
                logging.error(f"File {file.id} error: {file.last_error}")
            
            # Print first 10 files
            if len(file_statuses) <= 10:
                print(f"- {file.id} (added at: {file.created_at}{status_info})")
                
                # Check for errors on individual files
                if hasattr(file, 'last_error') and file.last_error:
                    print(f"  ⚠️ Error: {file.last_error}")
        
        if len(all_files_data) > 10:
            print(f"  ... and {len(all_files_data) - 10} more")
        
        # Print status summary if we have status information
        if file_statuses:
            logging.info(f"File Status Summary: {file_statuses}")
            print("\nFile Status Summary:")
            for status, count in file_statuses.items():
                print(f"- {status}: {count} files")
        
        # Check for any errors at the collection level
        if hasattr(vector_store_files, 'errors') and vector_store_files.errors:
            logging.error(f"Vector store errors: {vector_store_files.errors}")
            print("\nErrors found:")
            for error in vector_store_files.errors:
                print(f"- {error}")
        
        # Log failed files for potential retry
        if failed_files:
            logging.warning(f"Found {len(failed_files)} failed files")
            logging.info("Failed file IDs: " + ", ".join([f.id for f in failed_files]))
            
            # Ask if user wants to retry failed files
            print(f"\nFound {len(failed_files)} failed files. Use --retry-failed to attempt to fix them.")
        
        # Provide recommendations based on the mismatch
        if len(all_files_data) < len(local_files):
            print("\nRecommendations:")
            print("- Try using the --attach_files option to upload files one by one")
            print("- Check for API rate limits or quotas")
            print("- Verify that all files are valid markdown files")
            print("- Consider uploading files in smaller batches")
        elif len(all_files_data) > len(local_files):
            print("\nRecommendations:")
            print("- There are more files in the vector store than local files")
            print("- This could be due to duplicate uploads or files that were removed locally")
            print("- Consider recreating the vector store to ensure consistency")
        
        return len(all_files_data) == len(local_files), failed_files
        
    except Exception as e:
        logging.exception(f"Error verifying vector store: {str(e)}")
        print(f"Error verifying vector store: {str(e)}")
        return False, []

def verify_vector_store_simple():
    """
    Simple verification of vector store files using direct API call with pagination.
    
    Returns:
        list: List of file data or None if failed
    """
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return None
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        print("Error: No vector store ID found in config file")
        print("Please run with --update first to create a vector store")
        return None
    
    vector_store_id = config["vector_store_id"]
    print(f"Verifying vector store with ID: {vector_store_id}")
    
    try:
        # Get all files in the vector store with pagination
        all_files_data = []
        has_more = True
        after = None
        page = 1
        
        while has_more:
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
        
        # Create a formatted response similar to the example
        formatted_response = {
            "object": "list",
            "data": [],
            "first_id": all_files_data[0].id if all_files_data else None,
            "last_id": all_files_data[-1].id if all_files_data else None,
            "has_more": False  # We've fetched all pages
        }
        
        # Add file data
        for file in all_files_data:
            file_data = {
                "id": file.id,
                "object": "vector_store.file",
                "created_at": file.created_at,
                "vector_store_id": file.vector_store_id
            }
            
            # Add status if available
            if hasattr(file, 'status'):
                file_data["status"] = file.status
                
            # Add usage_bytes if available
            if hasattr(file, 'usage_bytes'):
                file_data["usage_bytes"] = file.usage_bytes
                
            formatted_response["data"].append(file_data)
        
        # Print the formatted response (first 5 and last 5 files for brevity)
        print("\nFormatted Vector Store Files Response (sample):")
        sample_response = formatted_response.copy()
        if len(formatted_response["data"]) > 10:
            sample_data = formatted_response["data"][:5] + [{"...": "..."}] + formatted_response["data"][-5:]
            sample_response["data"] = sample_data
        print(json.dumps(sample_response, indent=2))
        
        # Get all markdown files in the docs directory for comparison
        local_files = get_all_markdown_files()
        
        # Print a more readable summary
        print(f"\nSummary:")
        print(f"- Vector store ID: {vector_store_id}")
        print(f"- Files in vector store: {len(all_files_data)}")
        print(f"- Local markdown files: {len(local_files)}")
        
        # Check if all files are uploaded
        if len(all_files_data) == len(local_files):
            print("\n✅ All files appear to be uploaded to the vector store")
        else:
            print(f"\n⚠️ Mismatch: {len(local_files)} local files, but {len(all_files_data)} files in vector store")
        
        # Print file status summary
        status_counts = {}
        for file in all_files_data:
            if hasattr(file, 'status'):
                status = file.status
                status_counts[status] = status_counts.get(status, 0) + 1
        
        if status_counts:
            print("\nFile Status Summary:")
            for status, count in status_counts.items():
                print(f"- {status}: {count} files")
        
        return all_files_data
        
    except Exception as e:
        print(f"Error verifying vector store: {str(e)}")
        return None
