import pip._vendor.requests as requests


def test_create_log_text_file():
    response = requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile&directory=root&contents=test")
    assert response.status_code == 201
    assert response.json().get('message') == 'Created successfully.'
    assert response.json().get('file').get('contents') == 'test'
    assert type(response.json().get('file').get('directory')) is not None
    response = requests.post("http://127.0.0.1:5000/logtextfile?name=logtextfile&directory=root&contents=test")
    assert response.status_code == 400
    assert response.json().get('message') == 'Such file already exists.'


def test_if_log_file_deletable():
    response = requests.delete("http://127.0.0.1:5000/logtextfile?name=logtextfile")
    assert response.status_code == 200
    assert response.json().get('message') == 'Deleted successfully.'
    response = requests.delete("http://127.0.0.1:5000/logtextfile?name=logtextfile")
    assert response.status_code == 400
    assert response.json().get('message') == 'Deleting failed.'


def test_if_log_file_movable():
    response = requests.patch("http://127.0.0.1:5000/logtextfile?name=logtextfile&directory=root")
    assert response.status_code == 200
    assert response.json().get('message') == 'Moved successfully.'
    assert response.json().get('file').get('directory') == "root"


def test_if_line_appends():
    response = requests.patch("http://127.0.0.1:5000/logtextfile?name=logtextfile&append=test")
    assert response.status_code == 201
    assert response.json().get('message') == 'Line appended successfully.'
