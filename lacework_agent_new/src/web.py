"""
Web interface module for Lacework Agent.
Provides a web interface for interacting with the agent.
"""

import os
import logging
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

from .config import load_config
from .agent import ask_prompt, run_agent
from .utils import check_openai_api_key, vector_search

# Check if OpenAI Agents SDK is available
try:
    import asyncio
    from agents import Agent, Runner
    from .agent import run_agent_with_sdk
    AGENTS_SDK_AVAILABLE = True
except ImportError:
    AGENTS_SDK_AVAILABLE = False

# Create Flask app
app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
            static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'))

def create_app():
    """
    Create and configure the Flask app.
    
    Returns:
        Flask: The configured Flask app
    """
    # Load environment variables
    load_dotenv()
    
    # Register routes
    @app.route('/')
    def index():
        """Render the main page."""
        # Check if OpenAI API key is set
        api_key_set = check_openai_api_key()
        
        # Check if vector store exists
        config = load_config()
        vector_store_exists = config["vector_store_id"] is not None
        
        return render_template('index.html', 
                              api_key_set=api_key_set,
                              vector_store_exists=vector_store_exists,
                              agents_sdk_available=AGENTS_SDK_AVAILABLE)
    
    @app.route('/api/ask', methods=['POST'])
    def api_ask():
        """API endpoint for asking questions."""
        # Get request data
        data = request.json
        mode = data.get('mode', 'prompt')
        question = data.get('question', '')
        
        if not question:
            return jsonify({'error': 'Question is required'}), 400
        
        # Check if OpenAI API key is set
        if not check_openai_api_key():
            return jsonify({'error': 'OpenAI API key is not set'}), 400
        
        # Check if vector store exists
        config = load_config()
        if not config["vector_store_id"]:
            return jsonify({'error': 'Vector store does not exist. Please run with --update or --attach_files first.'}), 400
        
        try:
            # Process the question based on the selected mode
            if mode == 'prompt':
                # Use ask_prompt
                response = ask_prompt(question)
                return jsonify({'response': response})
            
            elif mode == 'agent':
                # Use run_agent
                response = run_agent(question)
                return jsonify({'response': response})
            
            elif mode == 'agentsdk':
                # Check if OpenAI Agents SDK is available
                if not AGENTS_SDK_AVAILABLE:
                    return jsonify({'error': 'OpenAI Agents SDK is not installed. Please install it with: pip install openai-agents'}), 400
                
                # Use run_agent_with_sdk
                # Since run_agent_with_sdk is async, we need to run it in an event loop
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                response = loop.run_until_complete(run_agent_with_sdk(question))
                loop.close()
                
                return jsonify({'response': response})
            
            else:
                return jsonify({'error': f'Invalid mode: {mode}'}), 400
        
        except Exception as e:
            logging.exception(f"Error processing question: {str(e)}")
            return jsonify({'error': f'Error processing question: {str(e)}'}), 500
    
    return app

def run_web_server(host='0.0.0.0', port=5000, debug=False):
    """
    Run the web server.
    
    Args:
        host (str): Host to run the server on
        port (int): Port to run the server on
        debug (bool): Whether to run in debug mode
    """
    app = create_app()
    app.run(host=host, port=port, debug=debug)
