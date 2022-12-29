import pip._vendor.requests as requests


def test_if_directory_creatable():
    response = requests.post("http://127.0.0.1:5000/directory?parent_directory=root&name=child&max_size=10")
    assert response.status_code == 201
    assert response.json().get('message') == 'Created successfully.'
    assert response.json().get('directory').get('max_size') == 10
    assert response.json().get('directory').get('count') == 0
    assert type(response.json().get('directory').get('parent_directory')) is not None
    response = requests.post("http://127.0.0.1:5000/directory?parent_directory=root&name=child&max_size=10")
    assert response.status_code == 400
    assert response.json().get('message') == 'Such directory already exists.'


def test_if_directory_deletable():
    response = requests.delete("http://127.0.0.1:5000/directory?name=child")
    assert response.status_code == 200
    assert response.json().get('message') == 'Deleted successfully.'
    response = requests.delete("http://127.0.0.1:5000/directory?name=child")
    assert response.status_code == 400
    assert response.json().get('message') == 'Deleting failed.'


def test_if_directory_movable():
    response = requests.patch("http://127.0.0.1:5000/directory?name=child&parentdirectory=root")
    assert response.status_code == 200
    assert response.json().get('message') == 'Moved successfully.'
    assert response.json().get('directory').get('parent_directory') == "root"

