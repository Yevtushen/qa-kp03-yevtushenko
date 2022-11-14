import pytest
from directory import Directory


@pytest.fixture
def testing_parent_directory():
    return Directory("parent", None)


@pytest.fixture()
def testing_directory():
    return Directory("current", testing_parent_directory())


def check_if_directory_deletes():
    current_d = testing_directory()
    current_d.__delete__()
    assert current_d not in locals()


def check_if_directory_movable(self):
    current_d = testing_directory()
    current_d.move(self.testing_parent_directory())
    assert current_d.parent_directory == self.testing_parent_directory
