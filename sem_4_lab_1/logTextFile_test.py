import pytest
from logTextFile import LogTextFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_log_file(testing_directory):
    return LogTextFile("log_f", testing_directory, 'text')


def test_if_log_file_deletable(testing_log_file):
    testing_log_file.delete()
    assert testing_log_file not in locals()


def test_if_log_file_movable(testing_log_file, testing_parent_directory):
    testing_log_file.move_log_file(testing_parent_directory)
    assert testing_log_file.directory == testing_parent_directory


def test_if_line_appends(testing_log_file):
    testing_log_file.append_line("line")
    assert "line" in testing_log_file.read_file()
    assert "\n" in testing_log_file.read_file()
