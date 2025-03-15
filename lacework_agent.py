#!/usr/bin/env python3
import os
import json
import argparse
import glob
import sys
import logging
import time
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Import OpenAI Agents SDK (if available)
try:
    from agents import Agent, Runner
    AGENTS_SDK_AVAILABLE = True
except ImportError:
    AGENTS_SDK_AVAILABLE = False

# Set up logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
log_filename = os.path.join(LOG_DIR, f"lacework_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

# Configuration file to store vector store ID
CONFIG_FILE = "lacework_vector_store_config.json"
DOCS_DIR = "lacework_cli_docs"

def load_config():
    """Load configuration from JSON file or return empty dict if file doesn't exist"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"vector_store_id": None}

def save_config(config):
    """Save configuration to JSON file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def create_vector_store(client, name="Lacework CLI Documentation"):
    """Create a new vector store and return its ID"""
    print(f"Creating vector store: {name}")
    vector_store = client.vector_stores.create(name=name)
    print(f"Vector store created with ID: {vector_store.id}")
    return vector_store

def upload_docs_to_vector_store(client, vector_store_id):
    """Upload all markdown files from lacework_cli_docs to the vector store"""
    # Get all markdown files in the docs directory
    file_paths = glob.glob(os.path.join(DOCS_DIR, "*.md"))
    
    if not file_paths:
        print(f"No markdown files found in {DOCS_DIR}")
        return
    
    print(f"Found {len(file_paths)} markdown files to upload")
    
    # Open file streams for all files
    file_streams = [open(path, "rb") for path in file_paths]
    
    try:
        # Upload files to vector store
        print("Uploading files to vector store...")
        file_batch = client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id,
            files=file_streams
        )
        
        # Print status and file counts
        print(f"Upload status: {file_batch.status}")
        print(f"File counts: {file_batch.file_counts}")
        
        return file_batch
    finally:
        # Close all file streams
        for stream in file_streams:
            stream.close()

def attach_file_to_vector_store(client, vector_store_id, file_path):
    """Attach a single file to the vector store and verify completion"""
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

def update_vector_store():
    """Main function to update the vector store (manage file uploads and prevent duplicates)"""
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store already exists
    if config["vector_store_id"]:
        logging.info(f"Using existing vector store with ID: {config['vector_store_id']}")
        print(f"Using existing vector store with ID: {config['vector_store_id']}")
        vector_store_id = config["vector_store_id"]
    else:
        # Create new vector store
        logging.info("Creating new vector store")
        vector_store = create_vector_store(client)
        vector_store_id = vector_store.id
        
        # Save vector store ID to config
        config["vector_store_id"] = vector_store_id
        save_config(config)
        logging.info(f"Saved vector store ID {vector_store_id} to {CONFIG_FILE}")
        print(f"Saved vector store ID to {CONFIG_FILE}")
    
    # Get all local files
    local_files = glob.glob(os.path.join(DOCS_DIR, "*.md"))
    local_filenames = [os.path.basename(f) for f in local_files]
    
    if not local_files:
        logging.warning(f"No markdown files found in {DOCS_DIR}")
        print(f"No markdown files found in {DOCS_DIR}")
        return
    
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

def attach_files_to_vector_store():
    """Attach files one by one to the vector store"""
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        logging.info("No vector store ID found in config file. Creating a new vector store.")
        print("No vector store ID found in config file. Creating a new vector store...")
        create_new_vector_store = True
    else:
        # Check if the vector store with the ID exists
        vector_store_id = config["vector_store_id"]
        logging.info(f"Found vector store ID in config: {vector_store_id}. Verifying it exists...")
        print(f"Found vector store ID in config: {vector_store_id}. Verifying it exists...")
        
        try:
            # Try to access the vector store to verify it exists
            client.vector_stores.files.list(vector_store_id=vector_store_id, limit=1)
            logging.info(f"Vector store exists with ID: {vector_store_id}")
            print(f"Using existing vector store with ID: {vector_store_id}")
            create_new_vector_store = False
        except Exception as e:
            logging.error(f"Vector store with ID {vector_store_id} not found or not accessible: {str(e)}")
            print(f"Vector store with ID {vector_store_id} not found or not accessible.")
            print("Creating a new vector store...")
            create_new_vector_store = True
    
    # Create a new vector store if needed
    if create_new_vector_store:
        # Create new vector store
        vector_store = create_vector_store(client)
        vector_store_id = vector_store.id
        
        # Save vector store ID to config
        config["vector_store_id"] = vector_store_id
        save_config(config)
        logging.info(f"Saved vector store ID {vector_store_id} to {CONFIG_FILE}")
        print(f"Saved vector store ID to {CONFIG_FILE}")
    
    # Get all markdown files in the docs directory that start with "lacework"
    file_paths = glob.glob(os.path.join(DOCS_DIR, "lacework*.md"))
    
    if not file_paths:
        logging.warning(f"No lacework markdown files found in {DOCS_DIR}")
        print(f"No lacework markdown files found in {DOCS_DIR}")
        return
    
    logging.info(f"Found {len(file_paths)} lacework markdown files to attach")
    print(f"Found {len(file_paths)} lacework markdown files to attach")
    
    # Get all files in the vector store
    logging.info(f"Checking for existing files in vector store...")
    print(f"Checking for existing files in vector store...")
    
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
                logging.info(f"File already attached to vector store")
                print(f"File already attached to vector store")
                continue
            
            # Attach existing file to vector store
            logging.info(f"Attaching existing file to vector store: {file_id}")
            print(f"Attaching existing file to vector store...")
            
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

def verify_vector_store(client=None, vector_store_id=None):
    """Verify that all files have been uploaded to the vector store"""
    # If client is not provided, initialize it
    if client is None:
        # Load environment variables (for OPENAI_API_KEY)
        load_dotenv()
        
        # Check if OPENAI_API_KEY is set
        if not os.getenv("OPENAI_API_KEY"):
            logging.error("OPENAI_API_KEY environment variable is not set")
            print("Error: OPENAI_API_KEY environment variable is not set")
            print("Please set it in your .env file or environment")
            return
        
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
            return
        
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
        local_files = glob.glob(os.path.join(DOCS_DIR, "*.md"))
        local_filenames = [os.path.basename(f) for f in local_files]
        
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
    """Simple verification of vector store files using direct API call with pagination"""
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        print("Error: No vector store ID found in config file")
        print("Please run with --update first to create a vector store")
        return
    
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
        local_files = glob.glob(os.path.join(DOCS_DIR, "*.md"))
        
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

def delete_vector_store_and_files():
    """Delete the vector store, all its files, and related OpenAI files"""
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    vector_store_exists = False
    
    # Check if vector store ID exists
    if config["vector_store_id"]:
        vector_store_id = config["vector_store_id"]
        vector_store_exists = True
        print(f"Preparing to delete vector store with ID: {vector_store_id}")
    else:
        print("No vector store ID found in config file")
        print("Skipping vector store deletion, but will still clean up OpenAI files")
    
    try:
        if vector_store_exists:
            # Step 1: Get all files in the vector store with pagination
            print("\nStep 1: Retrieving all files from the vector store...")
            all_files_data = []
            has_more = True
            after = None
            page = 1
            
            try:
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
                
                print(f"Found {len(all_files_data)} files in the vector store")
                
                # Step 2: Delete all files from the vector store
                print("\nStep 2: Deleting files from the vector store...")
                deleted_vs_files = 0
                
                for file in all_files_data:
                    try:
                        print(f"Deleting file {file.id} from vector store...")
                        deleted = client.vector_stores.files.delete(
                            vector_store_id=vector_store_id,
                            file_id=file.id
                        )
                        if deleted.deleted:
                            deleted_vs_files += 1
                            print(f"✅ Successfully deleted file {file.id} from vector store")
                        else:
                            print(f"⚠️ Failed to delete file {file.id} from vector store")
                    except Exception as e:
                        print(f"Error deleting file {file.id} from vector store: {str(e)}")
                
                print(f"Deleted {deleted_vs_files} out of {len(all_files_data)} files from the vector store")
                
                # Step 3: Delete the vector store
                print("\nStep 3: Deleting the vector store...")
                try:
                    deleted_vs = client.vector_stores.delete(vector_store_id=vector_store_id)
                    if deleted_vs.deleted:
                        print(f"✅ Successfully deleted vector store {vector_store_id}")
                    else:
                        print(f"⚠️ Failed to delete vector store {vector_store_id}")
                except Exception as e:
                    print(f"Error deleting vector store: {str(e)}")
                    print("The vector store may no longer exist. Continuing with cleanup...")
            except Exception as e:
                print(f"Error accessing vector store: {str(e)}")
                print("The vector store may no longer exist. Continuing with cleanup...")
        
        # Step 4: Delete all OpenAI files that start with "lacework_"
        print("\nStep 4: Deleting OpenAI files that start with 'lacework_'...")
        all_openai_files = client.files.list()
        lacework_files = [file for file in all_openai_files.data if file.filename.startswith("lacework_")]
        
        print(f"Found {len(lacework_files)} OpenAI files that start with 'lacework_'")
        deleted_openai_files = 0
        
        for file in lacework_files:
            try:
                print(f"Deleting OpenAI file {file.id} ({file.filename})...")
                deleted = client.files.delete(file_id=file.id)
                if deleted.deleted:
                    deleted_openai_files += 1
                    print(f"✅ Successfully deleted OpenAI file {file.id}")
                else:
                    print(f"⚠️ Failed to delete OpenAI file {file.id}")
            except Exception as e:
                print(f"Error deleting OpenAI file {file.id}: {str(e)}")
        
        print(f"Deleted {deleted_openai_files} out of {len(lacework_files)} OpenAI files")
        
        # Step 5: Remove the vector store ID from the config file
        if config["vector_store_id"]:
            print("\nStep 5: Removing vector store ID from config file...")
            config["vector_store_id"] = None
            save_config(config)
            print(f"✅ Successfully removed vector store ID from {CONFIG_FILE}")
        
        print("\nCleanup complete!")
        
    except Exception as e:
        print(f"Error during cleanup: {str(e)}")
        return

def retry_failed_files():
    """Retry uploading files that failed in the vector store"""
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        logging.error("No vector store ID found in config file")
        print("Error: No vector store ID found in config file")
        print("Please run with --update first to create a vector store")
        return
    
    vector_store_id = config["vector_store_id"]
    logging.info(f"Checking for failed files in vector store with ID: {vector_store_id}")
    print(f"Checking for failed files in vector store with ID: {vector_store_id}")
    
    # First, verify the vector store to identify failed files
    success, failed_files = verify_vector_store(client, vector_store_id)
    
    if not failed_files:
        logging.info("No failed files found to retry")
        print("No failed files found to retry")
        return
    
    logging.info(f"Found {len(failed_files)} failed files to retry")
    print(f"\nFound {len(failed_files)} failed files to retry")
    
    # Get all local files
    local_files = glob.glob(os.path.join(DOCS_DIR, "*.md"))
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

def ask_prompt(prompt):
    """Ask a question to the vector store and stream the response"""
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        logging.error("No vector store ID found in config file")
        print("Error: No vector store ID found in config file")
        print("Please run with --update or --attach_files first to create a vector store")
        return
    
    vector_store_id = config["vector_store_id"]
    logging.info(f"Using vector store with ID: {vector_store_id}")
    print(f"Using vector store with ID: {vector_store_id}")
    
    try:
        # Create a non-streaming response using the vector store
        logging.info(f"Sending prompt to OpenAI: {prompt}")
        print("\nSending prompt to OpenAI...\n")
        
        # Create a response
        response = client.responses.create(
            model="gpt-4o",
            input=prompt,
            tools=[{
                "type": "file_search",
                "vector_store_ids": [vector_store_id]
            }]
        )
        
        # Process the response
        print("\n" + "-" * 80)
        print("Response:")
        print("-" * 80 + "\n")
        
        # Print the response
        if hasattr(response, 'output') and response.output:
            for output_item in response.output:
                if hasattr(output_item, 'type') and output_item.type == 'message':
                    if hasattr(output_item, 'content') and output_item.content:
                        for content_item in output_item.content:
                            if hasattr(content_item, 'text'):
                                print(content_item.text)
                elif hasattr(output_item, 'type') and output_item.type == 'file_search_call':
                    print(f"File search call ID: {output_item.id}")
                    print(f"Status: {output_item.status}")
                    if hasattr(output_item, 'queries') and output_item.queries:
                        print(f"Queries: {', '.join(output_item.queries)}")
        else:
            print("No response content received.")
        
        print("\n" + "-" * 80)
        
    except Exception as e:
        logging.exception(f"Error processing prompt: {str(e)}")
        print(f"Error processing prompt: {str(e)}")

# Tracing configuration
TRACE_DIR = "traces"
os.makedirs(TRACE_DIR, exist_ok=True)

def save_trace(trace_data, trace_id=None):
    """Save trace data to a JSON file"""
    if trace_id is None:
        trace_id = f"trace_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    trace_file = os.path.join(TRACE_DIR, f"{trace_id}.json")
    with open(trace_file, 'w') as f:
        json.dump(trace_data, f, indent=2)
    
    logging.info(f"Trace saved to {trace_file}")
    print(f"Trace saved to {trace_file}")
    
    return trace_file


def run_agent(task, send_to_openai=False):
    """Run the agent to solve complex tasks and return bash commands with tracing"""
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        logging.error("No vector store ID found in config file")
        print("Error: No vector store ID found in config file")
        print("Please run with --update or --attach_files first to create a vector store")
        return
    
    vector_store_id = config["vector_store_id"]
    logging.info(f"Using vector store with ID: {vector_store_id}")
    print(f"Using vector store with ID: {vector_store_id}")
    
    # Initialize trace data
    trace_id = f"agent_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    trace_data = {
        "trace_id": trace_id,
        "task": task,
        "vector_store_id": vector_store_id,
        "timestamp_start": datetime.now().isoformat(),
        "steps": []
    }
    
    try:
        # First, try to get relevant information from the vector store
        logging.info(f"Searching for relevant information for task: {task}")
        print(f"\nSearching for relevant information for task: {task}")
        
        # Record step start
        step1_start = datetime.now().isoformat()
        
        # Get relevant information using the vector store
        relevant_info_response = client.responses.create(
            model="gpt-4o",
            input=f"Find information relevant to this task: {task}. Return only the most relevant information from the Lacework CLI documentation.",
            tools=[{
                "type": "file_search",
                "vector_store_ids": [vector_store_id]
            }]
        )
        
        # Extract relevant information from the response
        relevant_info = ""
        if hasattr(relevant_info_response, 'output') and relevant_info_response.output:
            for output_item in relevant_info_response.output:
                if hasattr(output_item, 'type') and output_item.type == 'message':
                    if hasattr(output_item, 'content') and output_item.content:
                        for content_item in output_item.content:
                            if hasattr(content_item, 'text'):
                                relevant_info += content_item.text + "\n"
        
        # Record step completion
        step1_end = datetime.now().isoformat()
        trace_data["steps"].append({
            "step_id": "search_vector_store",
            "timestamp_start": step1_start,
            "timestamp_end": step1_end,
            "input": f"Find information relevant to this task: {task}. Return only the most relevant information from the Lacework CLI documentation.",
            "output": relevant_info,
            "model": "gpt-4o",
            "tools_used": [{
                "type": "file_search",
                "vector_store_ids": [vector_store_id]
            }]
        })
        
        logging.info(f"Found relevant information: {relevant_info}")
        print(f"\nFound relevant information from documentation.")
        
        # Now, use the relevant information to generate bash commands
        logging.info(f"Generating bash commands for task: {task}")
        print(f"\nGenerating bash commands for task: {task}")
        
        # Record step start
        step2_start = datetime.now().isoformat()
        
        # Generate bash commands using the relevant information
        command_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Lacework CLI expert. Your task is to generate bash commands to solve the user's task. "
                               "Use the provided documentation information to inform your commands. "
                               "Format your response as a series of bash commands with comments explaining each step. "
                               "If you need to use variables, explain how to set them. "
                               "If you're unsure about any part, provide the most likely command but add a comment with your uncertainty."
                },
                {
                    "role": "user",
                    "content": f"Task: {task}\n\nRelevant documentation information:\n{relevant_info}"
                }
            ]
        )
        
        # Extract the bash commands from the response
        bash_commands = command_response.choices[0].message.content
        
        # Record step completion
        step2_end = datetime.now().isoformat()
        trace_data["steps"].append({
            "step_id": "generate_bash_commands",
            "timestamp_start": step2_start,
            "timestamp_end": step2_end,
            "input": f"Task: {task}\n\nRelevant documentation information:\n{relevant_info}",
            "output": bash_commands,
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a Lacework CLI expert. Your task is to generate bash commands to solve the user's task. "
                               "Use the provided documentation information to inform your commands. "
                               "Format your response as a series of bash commands with comments explaining each step. "
                               "If you need to use variables, explain how to set them. "
                               "If you're unsure about any part, provide the most likely command but add a comment with your uncertainty."
                },
                {
                    "role": "user",
                    "content": f"Task: {task}\n\nRelevant documentation information:\n{relevant_info}"
                }
            ]
        })
        
        # Print the bash commands
        print("\n" + "-" * 80)
        print("Bash Commands:")
        print("-" * 80 + "\n")
        print(bash_commands)
        print("\n" + "-" * 80)
        
        # Complete the trace
        trace_data["timestamp_end"] = datetime.now().isoformat()
        trace_data["status"] = "completed"
        trace_data["output"] = bash_commands
        
        # Save the trace locally
        trace_file = save_trace(trace_data, trace_id)
        print(f"\nTrace saved to: {trace_file}")
        
        # Send the trace to OpenAI if requested
        if send_to_openai:
            print("\nSending trace to OpenAI...")
            if send_trace_to_openai(trace_data):
                print("✅ Trace successfully sent to OpenAI")
            else:
                print("❌ Failed to send trace to OpenAI")
        
        return bash_commands
        
    except Exception as e:
        # Record error in trace
        trace_data["timestamp_end"] = datetime.now().isoformat()
        trace_data["status"] = "error"
        trace_data["error"] = str(e)
        
        # Save the trace
        trace_file = save_trace(trace_data, trace_id)
        
        logging.exception(f"Error running agent: {str(e)}")
        print(f"Error running agent: {str(e)}")
        print(f"\nTrace with error details saved to: {trace_file}")
        
        return None

async def run_agent_with_sdk(task):
    """Run the agent using the OpenAI Agents SDK"""
    if not AGENTS_SDK_AVAILABLE:
        logging.error("OpenAI Agents SDK is not installed. Please install it with: pip install openai-agents")
        print("Error: OpenAI Agents SDK is not installed. Please install it with: pip install openai-agents")
        return
    
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        logging.error("No vector store ID found in config file")
        print("Error: No vector store ID found in config file")
        print("Please run with --update or --attach_files first to create a vector store")
        return
    
    vector_store_id = config["vector_store_id"]
    logging.info(f"Using vector store with ID: {vector_store_id}")
    print(f"Using vector store with ID: {vector_store_id}")
    
    logging.info(f"Running agent with OpenAI Agents SDK for task: {task}")
    print(f"Running agent with OpenAI Agents SDK for task: {task}")
    
    try:
        # Import the necessary components from the agents SDK
        from agents import Agent, Runner
        
        # First, get relevant information from the vector store
        logging.info(f"Searching for relevant information for task: {task}")
        print(f"\nSearching for relevant information for task: {task}")
        
        # Get relevant information using the vector store
        relevant_info = _vector_search_function(client, vector_store_id, task)
        
        # Define the agent with instructions that include the relevant information
        agent = Agent(
            name="LaceworkAgent",
            instructions=f"""You are a Lacework CLI expert. Your task is to generate bash commands to solve the user's task.

Here is relevant information from the Lacework CLI documentation:

{relevant_info}

Format your response as a series of bash commands with comments explaining each step.
If you need to use variables, explain how to set them.
If you're unsure about any part, provide the most likely command but add a comment with your uncertainty."""
        )
        
        # Run the agent with the task
        result = await Runner.run(agent, task)
        
        # Print the result
        print("\n" + "-" * 80)
        print("Bash Commands (using OpenAI Agents SDK with vector search):")
        print("-" * 80 + "\n")
        print(result.final_output)
        print("\n" + "-" * 80)
        
        return result.final_output
    
    except Exception as e:
        logging.exception(f"Error running agent with SDK: {str(e)}")
        print(f"Error running agent with SDK: {str(e)}")
        return None

def _vector_search_function(client, vector_store_id, query):
    """Helper function to search the vector store and return results"""
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
        logging.exception(f"Error in vector search: {str(e)}")
        print(f"Error in vector search: {str(e)}")
        return f"Error searching vector store: {str(e)}"

def main():
    """Main entry point with argument parsing"""
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
    
    args = parser.parse_args()
    
    if args.agentsdk:
        if AGENTS_SDK_AVAILABLE:
            asyncio.run(run_agent_with_sdk(args.agentsdk))
        else:
            print("Error: OpenAI Agents SDK is not installed. Please install it with: pip install openai-agents")
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
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
