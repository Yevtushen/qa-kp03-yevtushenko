import pytest
from bufferFile import BufferFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_buffer_file(testing_directory):
    return BufferFile("buffer_f", testing_directory, 10)


def test_if_buffer_file_deletable(testing_buffer_file):
    testing_buffer_file.__del__()
    assert testing_buffer_file not in locals()


def test_if_buffer_file_movable(testing_buffer_file, testing_parent_directory):
    testing_buffer_file.move_buffer_file(testing_parent_directory)
    assert testing_buffer_file.directory == testing_parent_directory


def test_if_element_pushes(testing_buffer_file):
    element = 'element'
    testing_buffer_file.push_element(element)
    assert element in testing_buffer_file.contents


def test_if_element_consumes(testing_buffer_file):
    element = 'element'
    testing_buffer_file.push_element(element)
    testing_buffer_file.consume_element(element)
    assert element not in testing_buffer_file.contents
