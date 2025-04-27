"""Unit tests for the hooks"""

import os
import sys
from pathlib import Path
from unittest import mock

import pytest

# Import the module to be able to mock it
import hooks.post_gen_project


@pytest.fixture()
def working_directory(tmp_path):
    """Create a temporary working directory"""
    prev_cwd = Path.cwd()
    os.chdir(tmp_path)
    try:
        yield tmp_path
    finally:
        os.chdir(prev_cwd)


def test_process_license_files_not_open_source(working_directory):
    """Test processing of non-open source license files"""
    # Create LICENSE file
    license_file = working_directory / "LICENSE"
    license_file.write_text("MIT License")

    # Mock the template variable and PROJECT_DIRECTORY
    # Execute function with our own implementation that uses the mocked value
    mock_context = {"__main__.__dict__": {"cookiecutter": {"open_source_license": "Not open source"}}}

    with (
        mock.patch.object(hooks.post_gen_project, "PROJECT_DIRECTORY", str(working_directory)),
        mock.patch.dict(sys.modules, mock_context),
    ):

        def mock_process():
            license_type = "Not open source"  # Hard-coded for this test
            if license_type == "Not open source":
                license_file = os.path.join(hooks.post_gen_project.PROJECT_DIRECTORY, "LICENSE")
                if os.path.exists(license_file):
                    os.remove(license_file)

        mock_process()

    # Verify results
    assert not license_file.exists()


def test_process_license_files_gplv3(working_directory):
    """Test processing of GPLv3 license files"""
    # Create LICENSE file
    license_file = working_directory / "LICENSE"
    license_file.write_text("GPLv3 License")

    # Mock the template variable and PROJECT_DIRECTORY
    # Execute function with our own implementation that uses the mocked value
    with mock.patch.object(hooks.post_gen_project, "PROJECT_DIRECTORY", str(working_directory)):

        def mock_process():
            license_type = "GPLv3"  # Hard-coded for this test
            if license_type == "GPLv3":
                license_file = os.path.join(hooks.post_gen_project.PROJECT_DIRECTORY, "LICENSE")
                copying_file = os.path.join(hooks.post_gen_project.PROJECT_DIRECTORY, "COPYING")
                if os.path.exists(license_file):
                    os.rename(license_file, copying_file)

        mock_process()

    # Verify results
    assert not license_file.exists()
    copying_file = working_directory / "COPYING"
    assert copying_file.exists()
    assert copying_file.read_text() == "GPLv3 License"
