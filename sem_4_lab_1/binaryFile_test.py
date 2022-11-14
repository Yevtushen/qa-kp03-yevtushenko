import pytest
from binaryFile import BinaryFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_binary_file():
    return BinaryFile("binary", testing_directory)


def check_if_binary_file_deletes():
    binary_f = testing_binary_file()
    binary_f.__delete__()
    assert binary_f not in locals()


def check_if_binary_file_movable(self):
    binary_f = testing_binary_file()
    binary_f.move_binary_file(testing_parent_directory())
    assert binary_f.parent_directory == self.testing_parent_directory()
