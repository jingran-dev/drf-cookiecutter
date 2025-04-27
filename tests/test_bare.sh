#!/bin/sh
# This is a simple script that tests the drf-cookiecutter generated project
# It is meant to be run from the root directory of the repository, e.g.:
# sh tests/test_bare.sh

set -o errexit
set -x

# Create a cache directory
mkdir -p .cache/bare
cd .cache/bare

# Create the project using the default settings in cookiecutter.json
uv run cookiecutter ../../ --no-input --overwrite-if-exists "$@"
cd my-drf-project

# Create a virtual environment
python -m venv venv
. venv/bin/activate

# Install project dependencies
pip install -r requirements/base.txt
pip install -r requirements/develop.txt
pip install -r requirements/production.txt

# Run the project's tests
pytest

# Make sure the Django check doesn't raise any warnings
python manage.py check --fail-level WARNING

# Define color codes
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color

# Clean up
deactivate
echo -e "${GREEN}${BOLD}✓ Test completed successfully!${NC}"
