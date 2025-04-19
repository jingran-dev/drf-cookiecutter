#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path

# Get the absolute path of the current project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def run_command(command, cwd=None):
    """Run command and check result"""
    print(f"Executing command: {command}")
    result = subprocess.run(command, shell=True, cwd=cwd or PROJECT_DIRECTORY)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        sys.exit(result.returncode)



def process_license_files():
    """Process license files based on selected license"""
    license_type = "{{ cookiecutter.open_source_license }}"
    
    # If not open source, remove the LICENSE file
    if license_type == "Not open source":
        license_file = os.path.join(PROJECT_DIRECTORY, "LICENSE")
        if os.path.exists(license_file):
            os.remove(license_file)
            print("Removed LICENSE file as project is not open source")
    else:
        print(f"License file created with {license_type} license")


def generate_requirements_files():
    """Generate requirements files using uv"""
    # Create requirements directory if it doesn't exist
    requirements_dir = os.path.join(PROJECT_DIRECTORY, "requirements")
    if not os.path.exists(requirements_dir):
        os.makedirs(requirements_dir)
        print(f"Created requirements directory at {requirements_dir}")
    
    # Generate base.txt
    print("Generating base requirements file...")
    run_command("uv export --no-hashes --no-header --output-file requirements/base.txt --no-group dev --no-group prod")
    
    # Generate develop.txt
    print("Generating development requirements file...")
    run_command("uv export --no-hashes --no-header --output-file requirements/develop.txt --group dev")
    
    # Generate production.txt
    print("Generating production requirements file...")
    run_command("uv export --no-hashes --no-header --output-file requirements/production.txt --group prod")
    
    print("Requirements files generated successfully")

def init_git_repo():
    """Initialize Git repository"""
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        run_command("git init")
        print("Initialized Git repository")

def main():
    """Main function to execute all initialization steps"""
    print("Starting post-project initialization script...")
    
    # Process license files
    process_license_files()
    
    # Generate requirements files
    generate_requirements_files()
    
    # Initialize Git repository
    init_git_repo()
    
    print("Post-project initialization script completed!")

if __name__ == "__main__":
    main()
