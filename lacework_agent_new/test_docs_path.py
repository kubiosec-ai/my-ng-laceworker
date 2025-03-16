#!/usr/bin/env python3
"""
Test script to verify that the code can access the files in the parent directory's lacework_cli_docs folder.
"""

import os
from src.config import DOCS_DIR
from src.file_operations import get_lacework_files, get_file_basenames

if __name__ == "__main__":
    # Create a log file
    with open("docs_path_test_results.txt", "w") as log_file:
        log_file.write(f"DOCS_DIR is set to: {DOCS_DIR}\n")
        log_file.write(f"Absolute path: {os.path.abspath(DOCS_DIR)}\n")
        
        # Check if the directory exists
        if os.path.exists(DOCS_DIR):
            log_file.write(f"Directory exists: {DOCS_DIR}\n")
        else:
            log_file.write(f"Directory does not exist: {DOCS_DIR}\n")
        
        # Get all lacework files
        files = get_lacework_files()
        
        # Write the number of files found
        log_file.write(f"Found {len(files)} lacework files\n")
        
        # Write the first 5 file names (if any)
        if files:
            basenames = get_file_basenames(files)
            log_file.write("First 5 files:\n")
            for i, name in enumerate(basenames[:5]):
                log_file.write(f"  {i+1}. {name}\n")
        
        # Write all file paths
        log_file.write("\nAll file paths:\n")
        for file_path in files:
            log_file.write(f"  {file_path}\n")
    
    print(f"Test results written to docs_path_test_results.txt")
