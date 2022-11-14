import pytest
from bufferFile import BufferFile
from directory_test import testing_directory
from directory_test import testing_parent_directory


@pytest.fixture()
def testing_buffer_file():
    return BufferFile("buffer_f", testing_directory())


def check_if_buffer_file_deletes():
    buffer_f = testing_buffer_file()
    buffer_f.__delete__()
    assert buffer_f not in locals()


def check_if_buffer_file_movable(self):
    buffer_f = testing_buffer_file()
    buffer_f.move_binary_file(testing_parent_directory())
    assert buffer_f.parent_directory == self.testing_parent_directory()
