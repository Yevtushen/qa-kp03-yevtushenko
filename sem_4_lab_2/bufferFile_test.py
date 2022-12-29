import pip._vendor.requests as requests


def test_if_buffer_file_creatable():
    response = requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile")
    assert response.status_code == 201
    assert response.json().get('message') == 'Created successfully.'
    assert isinstance(response.json().get('file').get('contents'), list)
    assert response.json().get('file').get('max_size') == 100
    assert type(response.json().get('file').get('directory')) is not None
    response = requests.post("http://127.0.0.1:5000/bufferfile?directory=root&max_size=100&name=bufferfile")
    assert response.status_code == 400
    assert response.json().get('message') == 'Such file already exists.'


def test_if_buffer_file_deletable():
    response = requests.delete("http://127.0.0.1:5000/bufferfile?name=bufferfile")
    assert response.status_code == 200
    assert response.json().get('message') == 'Deleted successfully.'
    response = requests.delete("http://127.0.0.1:5000/bufferfile?name=bufferfile")
    assert response.status_code == 400
    assert response.json().get('message') == 'Deleting failed.'


def test_if_buffer_file_movable():
    response = requests.patch("http://127.0.0.1:5000/bufferfile?directory=root&name=bufferfile")
    assert response.status_code == 200
    assert isinstance(response.json().get('file').get('contents'), list)
    assert response.json().get('file').get('max_size') == 100
    assert response.json().get('file').get('directory') == "root"


def test_if_element_pushes():
    response = requests.patch("http://127.0.0.1:5000/bufferfile?name=bufferfile&push=test")
    assert response.status_code == 201
    assert response.json().get('message') == 'Line pushed successfully.'


def test_if_element_consumes():
    response = requests.patch("http://127.0.0.1:5000/bufferfile?name=bufferfile&consume=true")
    assert response.status_code == 200
    assert response.json().get('message') == 'Line consumed successfully.'
