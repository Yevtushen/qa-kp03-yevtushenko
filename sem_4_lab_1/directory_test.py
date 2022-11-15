import pytest
from directory import Directory


@pytest.fixture
def testing_parent_directory():
    return Directory("parent", None, 10)


@pytest.fixture()
def testing_directory():
    parent = testing_parent_directory()
    return Directory("current", parent, 10)


def test_if_directory_deletes(testing_directory):
    testing_directory.__delete__()
    assert testing_directory not in locals()


def test_if_directory_movable(testing_directory, testing_parent_directory):
    testing_directory.move(testing_parent_directory)
    assert testing_directory.parent_directory == testing_directory
