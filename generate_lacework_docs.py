import os
import subprocess
import re

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def sanitize_filename(name):
    # Remove URL patterns
    name = re.sub(r'http[s]?://\S+', '', name)
    # Replace invalid characters with underscores
    name = re.sub(r'[<>:"/\\|?*,]', '_', name)
    # Replace periods with underscores to avoid double dots in filenames
    name = re.sub(r'\.', '_', name)
    # Remove leading/trailing underscores
    return name.strip('_')

def generate_markdown(command, output_dir):
    help_output = run_command(f"{command} --help")
    command_name = sanitize_filename(command.replace(" ", "_"))
    file_path = os.path.join(output_dir, f"{command_name}.md")
    with open(file_path, 'w') as file:
        file.write(f"# `{command}`\n\n```\n{help_output}\n```\n")
    print(f"Generated {file_path}")

def main():
    output_dir = "lacework_cli_docs"
    os.makedirs(output_dir, exist_ok=True)

    # Generate documentation for the main command
    generate_markdown("lacework", output_dir)

    # Extract subcommands from the main help output
    main_help = run_command("lacework --help")
    subcommands = []
    for line in main_help.splitlines():
        if line.startswith("  ") and not line.strip().startswith("-"):
            subcommand = line.split()[0].strip()
            subcommands.append(subcommand)

    # Generate documentation for each subcommand
    for subcommand in subcommands:
        generate_markdown(f"lacework {subcommand}", output_dir)

        # Extract sub-subcommands
        sub_help = run_command(f"lacework {subcommand} --help")
        sub_subcommands = []
        for line in sub_help.splitlines():
            if line.startswith("  ") and not line.strip().startswith("-"):
                sub_subcommand = line.split()[0].strip()
                sub_subcommands.append(sub_subcommand)

        # Generate documentation for each sub-subcommand
        for sub_subcommand in sub_subcommands:
            generate_markdown(f"lacework {subcommand} {sub_subcommand}", output_dir)

if __name__ == "__main__":
    main()
