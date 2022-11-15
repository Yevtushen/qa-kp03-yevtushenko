import pytest
from bufferFile import BufferFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_buffer_file():
    return BufferFile("buffer_f", testing_directory, 10)


def test_if_buffer_file_deletes(testing_buffer_file):
    testing_buffer_file.__delete__()
    assert testing_buffer_file not in locals()


def test_if_buffer_file_movable(testing_buffer_file):
    testing_buffer_file.move_binary_file(testing_parent_directory)
    assert testing_buffer_file.directory == testing_parent_directory
