import pytest
from logTextFile import LogTextFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_log_file(testing_directory):
    return LogTextFile("log_f", testing_directory, 'text')


def test_if_log_file_deletable(testing_log_file):
    pass


def test_if_log_file_movable(testing_log_file, testing_parent_directory):
    pass


def test_if_line_appends(testing_log_file):
    pass
