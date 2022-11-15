import pytest
from binaryFile import BinaryFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_binary_file():
    return BinaryFile("binary", testing_directory, 'something')


def test_if_binary_file_deletes(testing_binary_file):
    testing_binary_file.__delete__()
    assert testing_binary_file not in locals()


def test_if_binary_file_movable(testing_binary_file):
    testing_binary_file.move_binary_file(testing_parent_directory)
    assert testing_binary_file.directory == testing_parent_directory
