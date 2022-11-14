import pytest
from logTextFile import LogTextFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_log_file():
    return LogTextFile("log_f", testing_directory)


def check_if_log_file_deletes():
    log_f = testing_log_file
    log_f.__delete__()
    assert log_f not in locals()


def check_if_log_file_movable(self):
    log_f = testing_log_file
    log_f.move_binary_file(testing_parent_directory())
    assert log_f.parent_directory == self.testing_parent_directory()


def check_if_line_appends():
    log_f = testing_log_file()
    log_f.append_line("line")
    assert "line" in log_f.read_file()
    assert "/n" in log_f.read_file()
