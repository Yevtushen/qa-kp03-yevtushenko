import pip._vendor.requests as requests


def test_if_binary_file_creatable():
    response = requests.post("http://127.0.0.1:5000/binaryfile?name=binaryfile&directory=root&contents=test")
    assert response.status_code == 201
    assert response.json().get('message') == 'Created successfully.'
    assert response.json().get('file').get('contents') == 'test'
    assert type(response.json().get('file').get('directory')) is not None
    response = requests.post("http://127.0.0.1:5000/binaryfile?name=binaryfile&directory=root&contents=test")
    assert response.status_code == 400
    assert response.json().get('message') == 'Such file already exists.'


def test_if_binary_file_deletable():
    response = requests.delete("http://127.0.0.1:5000/binaryfile?name=binaryfile")
    assert response.status_code == 200
    assert response.json().get('message') == 'Deleted successfully.'
    response = requests.delete("http://127.0.0.1:5000/binaryfile?name=binaryfile")
    assert response.status_code == 400
    assert response.json().get('message') == 'Deleting failed.'


def test_if_binary_file_movable():
    response = requests.patch("http://127.0.0.1:5000/binaryfile?name=binaryfile&directory=root")
    assert response.status_code == 200
    assert response.json().get('message') == 'Moved successfully.'
    assert response.json().get('file').get('directory') == "root"
