"""
Configuration module for Lacework Agent.
Handles loading and saving configuration settings.
"""

import os
import json
import logging

# Configuration file to store vector store ID
CONFIG_FILE = "lacework_vector_store_config.json"
DOCS_DIR = "../lacework_cli_docs"

def load_config():
    """
    Load configuration from JSON file or return empty dict if file doesn't exist.
    
    Returns:
        dict: Configuration dictionary with vector_store_id
    """
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Error parsing config file: {str(e)}")
            return {"vector_store_id": None}
        except Exception as e:
            logging.error(f"Error loading config file: {str(e)}")
            return {"vector_store_id": None}
    return {"vector_store_id": None}

def save_config(config):
    """
    Save configuration to JSON file.
    
    Args:
        config (dict): Configuration dictionary to save
    """
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        logging.info(f"Configuration saved to {CONFIG_FILE}")
    except Exception as e:
        logging.error(f"Error saving config file: {str(e)}")
