# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Setup

### Prerequisites

- Python {{ cookiecutter.python_version }}+
- pip

### Installation

1. Clone the repository

```bash
git clone <repository-url>
cd {{ cookiecutter.project_slug }}
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -e .
```

4. Run migrations

```bash
python manage.py migrate
```

5. Create a superuser

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

## API Documentation

The API documentation is available at `/api/docs/` when the server is running.

## License

{{ cookiecutter.open_source_license }}
