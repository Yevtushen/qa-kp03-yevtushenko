import pytest
from binaryFile import BinaryFile
from directory import Directory


@pytest.fixture
def testing_parent_directory():
    return Directory("parent", None, 10)


@pytest.fixture()
def testing_directory(testing_parent_directory):
    return Directory("current", testing_parent_directory, 10)


@pytest.fixture()
def testing_binary_file(testing_directory):
    return BinaryFile("binary", testing_directory, 'something')


def test_if_binary_file_deletes(testing_binary_file):
    testing_binary_file.__del__()
    assert testing_binary_file not in locals()


def test_if_binary_file_movable(testing_binary_file, testing_parent_directory):
    testing_binary_file.move_binary_file(testing_parent_directory)
    assert testing_binary_file.directory == testing_parent_directory
