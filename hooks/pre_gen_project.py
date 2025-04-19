#!/usr/bin/env python
import re
import sys

# Project name validation
MODULE_REGEX = r'^[_a-zA-Z][-_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: Project name (%s) can only contain letters, numbers, underscores, and hyphens, and must start with a letter or underscore.' % module_name)
    # Exit, terminate project generation
    sys.exit(1)

# Email validation
EMAIL_REGEX = r'^[^@]+@[^@]+\.[^@]+$'
email = '{{ cookiecutter.email }}'

if not re.match(EMAIL_REGEX, email):
    print('WARNING: Email address (%s) is not in the correct format.' % email)
    # This is just a warning, don't terminate project generation
    print('Continuing project generation...')

print('Pre-project generation validation passed!')
