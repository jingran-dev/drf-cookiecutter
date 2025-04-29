# DRF Cookiecutter

A Cookiecutter template for creating production-ready Django REST Framework projects quickly.

## Features

- For Django 5.2
- Works with Python 3.11, 3.12, and 3.13
- Optimized for API development with Django REST Framework
- Modern project structure with apps directory for better organization
- Secure by default with JWT authentication
- Custom user model ready to go
- Comprehensive soft delete implementation
- API documentation with drf-spectacular (Swagger/OpenAPI)
- Robust logging with Loguru
- Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for code quality
- Ruff for linting and formatting

## Usage

First, make sure you have Cookiecutter installed:

```bash
pip install cookiecutter
```

Then generate a new DRF project:

```bash
cookiecutter https://github.com/jingran-dev/drf-cookiecutter
```

You'll be prompted for some values. Provide them, and then a Django REST Framework project will be created for you.

## Options

- `project_name`: Your project's human-readable name
- `project_slug`: Your project's slug (used for directories and files)
- `description`: A brief description of the project
- `author_name`: Your name or your organization's name
- `email`: Your email or your organization's contact email
- `username_type`: Choose between username or email for authentication
- `open_source_license`: Choose your preferred license
- `python_version`: Choose Python version (3.11, 3.12, or 3.13)

## Development

To contribute to this cookiecutter template:

1. Fork this repository
2. Create a new branch for your changes
3. Make your changes
4. Run the tests with `tox`
5. Submit a pull request

## Testing

This project includes a test suite to ensure the template works correctly:

```bash
# Run all tests
tox

# Run specific test environments
tox -e py313
tox -e ruff
```

## License

MIT
