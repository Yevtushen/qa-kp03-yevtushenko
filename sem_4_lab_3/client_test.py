import requests
import pytest
from client import *
import click
from click.testing import CliRunner

@pytest.fixture(autouse=True)
def run_before_and_after_tests(tmpdir):
    try:
        yield  # this is where the testing happens
    finally:
        requests.post("http://127.0.0.1:5000/cleanup")


def test_if_directory_creatable():
    runner = CliRunner()
    result = runner.invoke(create_directory, ['root', 'child', '5'])
    assert result.exit_code == 0

def test_if_directory_movable():
    requests.post("http://127.0.0.1:5000/directory?name=testing&parent_directory=root&max_size=20")
    runner = CliRunner()
    result = runner.invoke(move_directory, ['root', 'testing'])
    assert result.exit_code == 0


def test_if_directory_deletable():
    requests.post("http://127.0.0.1:5000/directory?name=child&parent_directory=root&max_size=20")
    runner = CliRunner()
    result = runner.invoke(delete_directory, ['child'])
    assert result.exit_code == 0


def test_if_directory_reads():
    requests.post("http://127.0.0.1:5000/directory?name=child&parent_directory=root&max_size=20")
    runner = CliRunner()
    result = runner.invoke(list_directory, ['root', 'child', '20'])
    assert result.exit_code == 0


def test_if_binary_file_creatable():
    runner = CliRunner()
    result = runner.invoke(create_binary_file, ['root', 'binaryfile', 'test'])
    assert result.exit_code == 0


def test_if_binary_file_movable():
    requests.post("http://127.0.0.1:5000/binaryfile?name=binaryfile1&directory=root&contents=test")
    runner = CliRunner()
    result = runner.invoke(move_binary_file, ['root', 'binaryfile'])
    assert result.exit_code == 0


def test_if_binary_file_readable():
    requests.post("http://127.0.0.1:5000/binaryfile?name=binaryfile1&directory=root&contents=test")
    runner = CliRunner()
    result = runner.invoke(read_binary_file, ['root', 'binaryfile1', 'test'])
    assert result.exit_code == 0


def test_if_binary_file_deletable():
    requests.post("http://127.0.0.1:5000/binaryfile?name=binaryfile1&directory=root&contents=test")
    runner = CliRunner()
    result = runner.invoke(delete_binary_file, ['binaryfile1'])
    assert result.exit_code == 0


def test_if_buffer_file_creatable():
    runner = CliRunner()
    result = runner.invoke(create_buffer_file, ['root', 'bufferfile', '100'])
    assert result.exit_code == 0


def test_if_buffer_file_movable():
    requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile1")
    runner = CliRunner()
    result = runner.invoke(move_buffer_file, ['root', 'bufferfile1'])
    assert result.exit_code == 0


def test_if_element_pushes():
    requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile")
    runner = CliRunner()
    result = runner.invoke(push_buffer_file, ['bufferfile', 'test'])
    assert result.exit_code == 0


def test_if_element_consumes():
    requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile")
    requests.patch("http://127.0.0.1:5000/bufferfile?name=bufferfile&push=test")
    runner = CliRunner()
    result = runner.invoke(consume_buffer_file, ['bufferfile', 'test'])
    assert result.exit_code == 0


def test_if_buffer_file_deletable():
    requests.post("http://127.0.0.1:5000/bufferfile?max_size=100&name=bufferfile")
    runner = CliRunner()
    result = runner.invoke(delete_buffer_file, ['bufferfile'])
    assert result.exit_code == 0


def test_if_buffer_file_readable():
    requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile")
    requests.patch("http://127.0.0.1:5000/bufferfile?name=bufferfile&push=test")
    runner = CliRunner()
    result = runner.invoke(read_buffer_file, ['root', 'bufferfile', '100'])
    assert result.exit_code == 0


def test_create_log_text_file():
    runner = CliRunner()
    result = runner.invoke(create_log_text_file, ['root', 'logtextfile', 'test'])
    assert result.exit_code == 0


def test_if_log_file_movable():
    requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile1&directory=root&contents=test")
    runner = CliRunner()
    result = runner.invoke(move_log_text_file, ['root', 'logtextfile'])
    assert result.exit_code == 0
    requests.post("http://127.0.0.1:5000/cleanup")


def test_if_log_file_readable():
    requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile1&directory=root&contents=test")
    runner = CliRunner()
    result = runner.invoke(read_log_text_file, ['root', 'logtextfile1'])
    assert result.exit_code == 0


def test_if_line_appends():
    requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile&directory=root&contents=test")
    runner = CliRunner()
    result = runner.invoke(append_log_text_file, ['logtextfile', 'test'])
    assert result.exit_code == 0


def test_if_log_file_deletable():
    requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile&directory=root&contents=test")
    runner = CliRunner()
    result = runner.invoke(delete_log_text_file, ['logtextfile'])
    assert result.exit_code == 0
