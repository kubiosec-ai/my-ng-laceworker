import os
import glob

def combine_markdown_files(input_dir, output_file):
    """
    Combine all markdown files in the input directory into a single markdown file.
    
    Args:
        input_dir (str): Directory containing markdown files
        output_file (str): Path to the output file
    """
    # Get all markdown files in the input directory
    md_files = glob.glob(os.path.join(input_dir, "*.md"))
    
    # Sort the files to ensure consistent ordering
    md_files.sort()
    
    # Create the output file
    with open(output_file, 'w') as outfile:
        # Write a header for the combined file
        outfile.write("# Lacework CLI Documentation\n\n")
        outfile.write("This file contains combined documentation for all Lacework CLI commands.\n\n")
        outfile.write("## Table of Contents\n\n")
        
        # Create a table of contents
        for md_file in md_files:
            filename = os.path.basename(md_file)
            command_name = filename.replace('.md', '').replace('_', ' ')
            outfile.write(f"- [{command_name}](#{command_name.lower().replace(' ', '-')})\n")
        
        outfile.write("\n---\n\n")
        
        # Write the content of each file
        for md_file in md_files:
            filename = os.path.basename(md_file)
            command_name = filename.replace('.md', '').replace('_', ' ')
            
            # Add a section header
            outfile.write(f"## {command_name}\n\n")
            
            # Read and write the content of the file
            with open(md_file, 'r') as infile:
                content = infile.read()
                # Skip the first line if it's a header (to avoid duplicate headers)
                if content.startswith('# '):
                    content = content.split('\n', 1)[1].strip()
                outfile.write(content)
                outfile.write("\n\n---\n\n")  # Add a separator between files

if __name__ == "__main__":
    input_dir = "lacework_cli_docs"
    output_file = "help.txt"
    
    combine_markdown_files(input_dir, output_file)
    print(f"Combined {len(glob.glob(os.path.join(input_dir, '*.md')))} markdown files into {output_file}")
