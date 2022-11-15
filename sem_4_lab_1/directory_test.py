import pytest
from directory import Directory


@pytest.fixture
def testing_parent_directory():
    return Directory("parent", None, 10)


@pytest.fixture()
def testing_directory(testing_parent_directory):
    return Directory("current", testing_parent_directory, 10)


def test_if_directory_deletes(testing_directory):
    testing_directory.__del__()
    assert testing_directory not in locals()


def test_if_directory_movable(testing_directory, testing_parent_directory):
    testing_directory.move_directory(testing_parent_directory)
    assert testing_directory.parent_directory == testing_parent_directory
