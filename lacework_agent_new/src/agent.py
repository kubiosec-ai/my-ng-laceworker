"""
Agent module for Lacework Agent.
Handles agent operations for interacting with the vector store.
"""

import os
import logging
import json
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

from .config import load_config
from .utils import save_trace, vector_search

# Check if OpenAI Agents SDK is available
try:
    from agents import Agent as OpenAIAgent, Runner
    AGENTS_SDK_AVAILABLE = True
except ImportError:
    AGENTS_SDK_AVAILABLE = False

def ask_prompt(prompt):
    """
    Ask a question to the vector store and get a response.
    
    Args:
        prompt (str): The prompt to send to the vector store
        
    Returns:
        str: The response from the vector store
    """
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return None
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        logging.error("No vector store ID found in config file")
        print("Error: No vector store ID found in config file")
        print("Please run with --update or --attach_files first to create a vector store")
        return None
    
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
        
        # Extract and format the response text
        response_text = ""
        
        # Print the response
        if hasattr(response, 'output') and response.output:
            for output_item in response.output:
                if hasattr(output_item, 'type') and output_item.type == 'message':
                    if hasattr(output_item, 'content') and output_item.content:
                        for content_item in output_item.content:
                            if hasattr(content_item, 'text'):
                                response_text += content_item.text + "\n"
                                print(content_item.text)
                elif hasattr(output_item, 'type') and output_item.type == 'file_search_call':
                    file_search_info = f"File search call ID: {output_item.id}\n"
                    file_search_info += f"Status: {output_item.status}\n"
                    
                    if hasattr(output_item, 'queries') and output_item.queries:
                        file_search_info += f"Queries: {', '.join(output_item.queries)}\n"
                    
                    response_text += file_search_info
                    print(file_search_info)
        else:
            no_content_msg = "No response content received."
            response_text += no_content_msg
            print(no_content_msg)
        
        print("\n" + "-" * 80)
        
        return response_text
        
    except Exception as e:
        error_msg = f"Error processing prompt: {str(e)}"
        logging.exception(error_msg)
        print(error_msg)
        return error_msg

def run_agent(task, send_to_openai=False):
    """
    Run the agent to solve complex tasks and return bash commands with tracing.
    
    Args:
        task (str): The task to solve
        send_to_openai (bool): Whether to send the trace to OpenAI
        
    Returns:
        str: The bash commands to solve the task
    """
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return None
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        logging.error("No vector store ID found in config file")
        print("Error: No vector store ID found in config file")
        print("Please run with --update or --attach_files first to create a vector store")
        return None
    
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
                               "Use --json flag to avoid any."
                               "Do not assume anything. "
                               "Use rfc3339 format for time --start and --end. Do not create ranges larger then 7 days"
                              

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
            # This functionality would need to be implemented in the future
            print("⚠️ Sending traces to OpenAI is not yet implemented")
        
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
    """
    Run the agent using the OpenAI Agents SDK.
    
    Args:
        task (str): The task to solve
        
    Returns:
        str: The output from the agent
    """
    if not AGENTS_SDK_AVAILABLE:
        logging.error("OpenAI Agents SDK is not installed. Please install it with: pip install openai-agents")
        print("Error: OpenAI Agents SDK is not installed. Please install it with: pip install openai-agents")
        return None
    
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set")
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        return None
    
    # Initialize OpenAI client
    client = OpenAI()
    
    # Load existing configuration
    config = load_config()
    
    # Check if vector store ID exists
    if not config["vector_store_id"]:
        logging.error("No vector store ID found in config file")
        print("Error: No vector store ID found in config file")
        print("Please run with --update or --attach_files first to create a vector store")
        return None
    
    vector_store_id = config["vector_store_id"]
    logging.info(f"Using vector store with ID: {vector_store_id}")
    print(f"Using vector store with ID: {vector_store_id}")
    
    logging.info(f"Running agent with OpenAI Agents SDK for task: {task}")
    print(f"Running agent with OpenAI Agents SDK for task: {task}")
    
    try:
        # First, get relevant information from the vector store
        logging.info(f"Searching for relevant information for task: {task}")
        print(f"\nSearching for relevant information for task: {task}")
        
        # Get relevant information using the vector store
        relevant_info = vector_search(client, vector_store_id, task)
        
        # Define the agent with instructions that include the relevant information
        agent = OpenAIAgent(
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
