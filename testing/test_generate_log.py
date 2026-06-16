# testing/test_generate_log.py

import os
import pytest
from datetime import datetime
from lib.generate_log import generate_log

@pytest.fixture
def log_data():
    return ["Entry one", "Entry two", "Entry three"]

@pytest.fixture
def generated_file(log_data):
    filename = generate_log(log_data)
    yield filename
    if os.path.exists(filename):
        os.remove(filename)

def test_log_file_created(generated_file):
    """Test that the log file is created with today's date in the filename."""
    assert os.path.exists(generated_file), f"{generated_file} not found."

def test_log_file_name_format(generated_file):
    """Test that the filename follows the expected naming convention."""
    today = datetime.now().strftime("%Y%m%d")
    assert generated_file == f"log_{today}.txt", "Filename does not match expected format."

def test_log_file_content_matches_input(generated_file, log_data):
    """Test that the content written to the log matches the input list."""
    with open(generated_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    assert lines == log_data, "Log file contents do not match input data."

def test_generate_log_raises_error_on_invalid_input():
    """Test that the function raises a ValueError when input is not a list."""
    with pytest.raises(ValueError):
        generate_log("This should be a list")

def test_empty_log_list_creates_empty_file():
    """Test that passing an empty list still creates an empty log file."""
    filename = generate_log([])
    with open(filename, "r") as file:
        content = file.read()
    assert content == ""
    os.remove(filename)

def test_generate_log_prints_confirmation_message(log_data, capsys):
    """Test that the function prints a confirmation message with the filename."""
    filename = generate_log(log_data)
    captured = capsys.readouterr()
    assert f"Log written to {filename}" in captured.out
    os.remove(filename)

def test_log_file_created_in_expected_directory_and_removed(log_data):
    """Test that the log file is created in cwd and can be removed cleanly."""
    filename = generate_log(log_data)
    expected_path = os.path.join(os.getcwd(), filename)

    assert os.path.abspath(filename) == expected_path
    assert os.path.exists(expected_path)

    os.remove(expected_path)
    assert not os.path.exists(expected_path)
