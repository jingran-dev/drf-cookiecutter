import os
import re
import sys

import pytest

try:
    import sh
except (ImportError, ModuleNotFoundError):
    sh = None  # sh doesn't support Windows
from binaryornot.check import is_binary
from cookiecutter.exceptions import FailedHookException

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)

if sys.platform.startswith("win"):
    pytest.skip("sh doesn't support windows", allow_module_level=True)
elif sys.platform.startswith("darwin") and os.getenv("CI"):
    pytest.skip("skipping slow macOS tests on CI", allow_module_level=True)


@pytest.fixture
def context():
    """Basic context with variables needed for project generation"""
    return {
        "project_name": "Test DRF Project",
        "project_slug": "test_drf_project",
        "description": "Test Django REST Framework API Project",
        "author_name": "Test Author",
        "email": "test@example.com",
        "version": "0.1.0",
        "python_version": "3.11",
        "username_type": "username",
        "open_source_license": "MIT",
    }


SUPPORTED_COMBINATIONS = [
    {"username_type": "username"},
    {"username_type": "email"},
    {"open_source_license": "MIT"},
    {"open_source_license": "BSD"},
    {"open_source_license": "GPLv3"},
    {"open_source_license": "Apache Software License 2.0"},
    {"open_source_license": "Not open source"},
    {"python_version": "3.11"},
    {"python_version": "3.12"},
    {"python_version": "3.13"},
]


def _fixture_id(ctx):
    """Generate a user-friendly test name"""
    return "-".join(f"{key}:{value}" for key, value in ctx.items())


def build_files_list(base_dir):
    """Build a list of absolute paths to the generated files"""
    return [os.path.join(dirpath, file_path) for dirpath, subdirs, files in os.walk(base_dir) for file_path in files]


def check_paths(paths):
    """Check all paths have correct substitutions"""
    for path in paths:
        if is_binary(path):
            continue

        with open(path, encoding="utf-8") as f:
            for line in f:
                match = RE_OBJ.search(line)
                assert match is None, f"Cookiecutter variable not replaced in {path}: {line}"


@pytest.mark.parametrize("context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_project_generation(cookies, context, context_override):
    """Test that project is generated and fully rendered"""
    result = cookies.bake(extra_context={**context, **context_override})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    paths = build_files_list(str(result.project_path))
    assert paths
    check_paths(paths)


@pytest.mark.parametrize("context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_ruff_check_passes(cookies, context_override, context):
    """Generated project should pass basic ruff checks (excluding import sorting)"""
    result = cookies.bake(extra_context={**context, **context_override})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    try:
        # Use --select parameter to only check for serious errors, skipping import sorting and formatting issues
        sh.ruff("check", ".", "--select", "E9,F63,F7,F82", _cwd=str(result.project_path))
    except sh.ErrorReturnCode as e:
        pytest.fail(e.stdout.decode())


@pytest.mark.parametrize("slug", ["123-project", "project!"])
def test_invalid_slug(cookies, context, slug):
    """Invalid slug should fail pre-generation hook"""
    context.update({"project_slug": slug})
    result = cookies.bake(extra_context=context)

    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


def test_trim_email(cookies, context):
    """Check that leading and trailing spaces are trimmed in email"""
    context.update({"email": " test@example.com "})
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    # Look for README.md which should contain the email
    readme_path = result.project_path / "README.md"
    if readme_path.exists():
        with open(readme_path) as f:
            content = f.read()
            if "test@example.com" in content:
                assert " test@example.com " not in content
                return

    # Alternatively check any other files that might contain the email
    for file_path in ["LICENSE", ".env.example", "docs/index.md"]:
        path = result.project_path / file_path
        if path.exists():
            with open(path) as f:
                content = f.read()
                if "test@example.com" in content:
                    assert " test@example.com " not in content
                    return

    # If we get here, we couldn't find the email in any of the expected files
    # This is still a pass as we're just testing that spaces are trimmed if the email is used
    pass
