import pytest
from binaryFile import BinaryFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_binary_file(testing_directory):
    return BinaryFile("binary", testing_directory, 'something')


def test_if_binary_file_deletable(testing_binary_file):
    pass


def test_if_binary_file_movable(testing_binary_file, testing_parent_directory):
    pass
