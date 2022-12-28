import pytest
from bufferFile import BufferFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_buffer_file(testing_directory):
    return BufferFile("buffer_f", testing_directory, 10)


def test_if_buffer_file_deletable(testing_buffer_file):
    pass


def test_if_buffer_file_movable(testing_buffer_file, testing_parent_directory):
    pass


def test_if_element_pushes(testing_buffer_file):
    pass


def test_if_element_consumes(testing_buffer_file):
    pass
