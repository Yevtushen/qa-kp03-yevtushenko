import pytest
from bufferFile import BufferFile
from directory import Directory


@pytest.fixture
def testing_parent_directory():
    return Directory("parent", None, 10)


@pytest.fixture()
def testing_directory(testing_parent_directory):
    return Directory("current", testing_parent_directory, 10)


@pytest.fixture()
def testing_buffer_file(testing_directory):
    return BufferFile("buffer_f", testing_directory, 10)


def test_if_buffer_file_deletes(testing_buffer_file):
    testing_buffer_file.__del__()
    assert testing_buffer_file not in locals()


def test_if_buffer_file_movable(testing_buffer_file, testing_parent_directory):
    testing_buffer_file.move_buffer_file(testing_parent_directory)
    assert testing_buffer_file.directory == testing_parent_directory
