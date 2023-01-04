import requests
import pytest

@pytest.fixture(autouse=True)
def run_before_and_after_tests(tmpdir):
    try:
        yield  # this is where the testing happens
    finally:
        requests.post("http://127.0.0.1:5000/cleanup")


def test_if_directory_creatable():
    response = requests.post("http://127.0.0.1:5000/directory?name=child&parent_directory=root&max_size=10")
    assert response.status_code == 201
    assert response.json().get('message') == 'Created successfully.'
    assert response.json().get('directory').get('max_size') == 10
    assert type(response.json().get('directory').get('parent_directory')) is not None
    response = requests.post("http://127.0.0.1:5000/directory?parent_directory=root&name=child&max_size=10")
    assert response.status_code == 400
    assert response.json().get('message') == 'Such directory already exists.'


def test_if_directory_movable():
    requests.post("http://127.0.0.1:5000/directory?name=testing&parent_directory=root&max_size=20")
    response = requests.patch("http://127.0.0.1:5000/directory?name=testing&parent_directory=root")
    assert response.status_code == 200
    assert response.json().get('message') == 'Moved successfully.'
    assert response.json().get('directory').get('parent_directory') == "root"

def test_if_directory_deletable():
    requests.post("http://127.0.0.1:5000/directory?name=child&parent_directory=root&max_size=20")
    response = requests.delete("http://127.0.0.1:5000/directory?name=child")
    assert response.status_code == 200
    assert response.json().get('message') == 'Deleted successfully.'
    response = requests.delete("http://127.0.0.1:5000/directory?name=child")
    assert response.status_code == 400
    assert response.json().get('message') == 'Deleting failed.'

def test_if_binary_file_creatable():
    response = requests.post("http://127.0.0.1:5000/binaryfile?name=binaryfile&directory=root&contents=test")
    assert response.status_code == 201
    assert response.json().get('message') == 'Created successfully.'
    assert response.json().get('file').get('contents') == 'test'
    print(type(response.json().get('file').get('directory')))
    assert type(response.json().get('file').get('directory')) is not None
    response = requests.post("http://127.0.0.1:5000/binaryfile?name=binaryfile&directory=root&contents=test")
    assert response.status_code == 400
    assert response.json().get('message') == 'Such file already exists.'

def test_if_binary_file_movable():
    requests.post("http://127.0.0.1:5000/binaryfile?name=binaryfile1&directory=root&contents=test")
    response = requests.patch("http://127.0.0.1:5000/binaryfile?name=binaryfile1&directory=root")
    assert response.status_code == 200
    assert response.json().get('message') == 'Moved successfully.'
    assert response.json().get('file').get('directory') == "root"

def test_if_binary_file_deletable():
    requests.post("http://127.0.0.1:5000/binaryfile?name=binaryfile1&directory=root&contents=test")
    response = requests.delete("http://127.0.0.1:5000/binaryfile?name=binaryfile1")
    assert response.status_code == 200
    assert response.json().get('message') == 'Deleted successfully.'
    response = requests.delete("http://127.0.0.1:5000/binaryfile?name=binaryfile1")
    assert response.status_code == 400
    assert response.json().get('message') == 'Deleting failed.'

def test_if_buffer_file_creatable():
    response = requests.post("http://127.0.0.1:5000/bufferfile?max_size=100&name=bufferfile")
    assert response.status_code == 201
    assert response.json().get('message') == 'Created successfully.'
    assert isinstance(response.json().get('file').get('contents'), list)
    assert response.json().get('file').get('max_size') == 100
    assert type(response.json().get('file').get('directory')) is not None
    response = requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile")
    assert response.status_code == 400
    assert response.json().get('message') == 'Such file already exists.'


def test_if_buffer_file_movable():
    requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile1")
    response = requests.patch("http://127.0.0.1:5000/bufferfile?directory=root&name=bufferfile1")
    assert response.status_code == 200
    assert isinstance(response.json().get('file').get('contents'), list)
    assert response.json().get('file').get('max_size') == 100
    assert response.json().get('file').get('directory') == "root"


def test_if_element_pushes():
    requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile")
    response = requests.patch("http://127.0.0.1:5000/bufferfile?name=bufferfile&push=test")
    assert response.status_code == 201
    assert response.json().get('message') == 'Element pushed successfully.'


def test_if_element_consumes():
    requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile")
    requests.patch("http://127.0.0.1:5000/bufferfile?name=bufferfile&push=test")
    response = requests.patch("http://127.0.0.1:5000/bufferfile?name=bufferfile&consume=test")
    assert response.status_code == 200
    assert response.json().get('message') == 'Element consumed successfully.'


def test_if_buffer_file_deletable():
    requests.post("http://127.0.0.1:5000/bufferfile?max_size=100&name=bufferfile")
    response = requests.delete("http://127.0.0.1:5000/bufferfile?name=bufferfile")
    assert response.status_code == 200
    assert response.json().get('message') == 'Deleted successfully.'
    response = requests.delete("http://127.0.0.1:5000/bufferfile?name=bufferfile")
    assert response.status_code == 400
    assert response.json().get('message') == 'Deleting failed.'

def test_create_log_text_file():
    response = requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile&directory=root&contents=test")
    assert response.status_code == 201
    assert response.json().get('message') == 'Created successfully.'
    assert response.json().get('file').get('contents') == 'test'
    assert type(response.json().get('file').get('directory')) is not None
    response = requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile&directory=root&contents=test")
    assert response.status_code == 400
    assert response.json().get('message') == 'Such file already exists.'


def test_if_log_file_movable():
    requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile1&directory=root&contents=test")
    response = requests.patch("http://127.0.0.1:5000/logtextfile?name=logtextfile1&directory=root")
    assert response.status_code == 200
    assert response.json().get('message') == 'Moved successfully.'
    assert response.json().get('file').get('directory') == "root"
    requests.post("http://127.0.0.1:5000/cleanup")


def test_if_line_appends():
    requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile&directory=root&contents=test")
    response = requests.patch("http://127.0.0.1:5000/logtextfile?name=logtextfile&append=test")
    assert response.status_code == 201
    assert response.json().get('message') == 'Line appended successfully.'

def test_if_log_file_deletable():
    requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile&directory=root&contents=test")
    response = requests.delete("http://127.0.0.1:5000/logtextfile?name=logtextfile")
    assert response.status_code == 200
    assert response.json().get('message') == 'Deleted successfully.'
    response = requests.delete("http://127.0.0.1:5000/logtextfile?name=logtextfile")
    assert response.status_code == 400
    assert response.json().get('message') == 'Deleting failed.'

