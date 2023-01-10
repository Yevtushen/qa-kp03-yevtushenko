from flask import Flask, jsonify, request
from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile

app = Flask(__name__)

root = Directory('root', None, 100)
trash = []


@app.route('/cleanup', methods=['POST'])
def cleanup():
    global root, trash
    root = Directory('root', None, 100)
    trash = []
    return None


def directory_post(request):
    if any(element.name == request.args.get('name') for element in root.list) or request.args.get('name') == 'root':
        return jsonify({'message': 'Such directory already exists.'}), 400
    dir = Directory(request.args.get('name'), root, int(request.args.get('max_size')))
    return jsonify({
        'message': 'Created successfully.',
        'directory': {
            'parent_directory': dir.parent_directory.name,
            'name': dir.name,
            'max_size': int(dir.max_size)
        }
    }), 201


def directory_get(request):
    if any(dir.name == request.args.get('name') for dir in root.list) or request.args.get('name') == 'root':
        if request.args.get('name') == 'root':
            dir = root
        else:
            dir = next(element for element in root.list if element.name == request.args.get('name'))
        return jsonify({
            'message': 'Read successfully.',
            'directory': {
                'parent_directory': dir.parent_directory.name,
                'name': dir.name,
                'max_size': dir.max_size
            }
        }), 200
    return jsonify({'message': 'Directory does not exist.', }), 400


def directory_patch(request):
    if any(dir.name == request.args.get('name') for dir in root.list):
        dir = next(element for element in root.list if element.name == request.args.get('name'))
        dir.move_directory(root)
        return jsonify({
            'message': 'Moved successfully.',
            'directory': {
                'parent_directory': dir.parent_directory.name,
                'name': dir.name,
                'max_size': dir.max_size
            }
        }), 200
    return jsonify({'message': 'Directory does not exist.', }), 400


def directory_delete(request):
    if request.args.get('name') not in trash and any(dir.name == request.args.get('name') for dir in root.list):
        dir = next(x for x in root.list if x.name == request.args.get('name'))
        dir.delete()
        trash.append(request.args.get('name'))
        return jsonify({
            'message': 'Deleted successfully.',
        }), 200
    return jsonify({'message': 'Deleting failed.'}), 400


@app.route('/directory', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def directory():
    if request.method == 'POST':
        return directory_post(request)
    elif request.method == 'GET':
        return directory_get(request)
    elif request.method == 'PATCH':
        return directory_patch(request)
    else:
        return directory_delete(request)


def binary_file_post(request):
    if any(element.name == request.args.get('name') for element in root.list):
        return jsonify({
            'message': 'Such file already exists.',
        }), 400
    file = BinaryFile(request.args.get('name'), root, request.args.get('contents'))
    return jsonify({
        'message': 'Created successfully.',
        'file': {
            'directory': file.directory.name,
            'name': file.name,
            'contents': file.contents
        }
    }), 201


def binary_file_get(request):
    if any(file.name == request.args.get('name') for file in root.list):
        file = next(element for element in root.list if element.name == request.args.get('name'))
        return jsonify({
            'message': 'Read successfully.',
            'file': {
                'directory': file.directory.name,
                'name': file.name,
                'contents': file.contents
            }
        }), 200
    return jsonify({'message': "Such file does not exist."}), 400


def binary_file_delete(request):
    if request.args.get('name') not in trash and any(file.name == request.args.get('name') for file in root.list):
        file = next(x for x in root.list if x.name == request.args.get('name'))
        file.delete()
        trash.append(request.args.get('name'))
        return jsonify({'message': "Deleted successfully."}), 200
    return jsonify({"message": "Deleting failed."}), 400


def binary_file_patch(request):
    if any(file.name == request.args.get('name') for file in root.list):
        file = next(element for element in root.list if element.name == request.args.get('name'))
        file.move_binary_file(root)
        return jsonify({
            'message': 'Moved successfully.',
            'file': {
                'directory': file.directory.name,
                'name': file.name,
                'content': file.contents
            }
        }), 200
    return jsonify({'message': "Such file does not exist."}), 400


@app.route('/binaryfile', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def binaryfile():
    # file = BinaryFile(request.args.get('name'), root, request.args.get('contents'))
    if request.method == 'POST':
        return binary_file_post(request)
    elif request.method == 'GET':
        return binary_file_get(request)
    elif request.method == 'PATCH':
        return binary_file_patch(request)
    else:
        return binary_file_delete(request)


def logTextFilePost(request):
    if any(element.name == request.args.get('name') for element in root.list):
        return jsonify({
            'message': "Such file already exists.",
        }), 400
    file = LogTextFile(request.args.get('name'), root, request.args.get('contents'))
    return jsonify({
        'message': "Created successfully.",
        'file': {
            'directory': file.directory.name,
            'name': file.name,
            'contents': file.contents
        }
    }), 201


def log_text_file_get(request):
    if any(file.name == request.args.get('name') for file in root.list):
        file = next(element for element in root.list if element.name == request.args.get('name'))
        return jsonify({
            'message': "Read successfully.",
            'file': {
                'directory': file.directory.name,
                'name': file.name,
                'contents': file.contents
            }
        }), 200
    return jsonify({'message': 'Such file does not exist.'}), 400


def log_text_file_patch(request):
    if any(file.name == request.args.get('name') for file in root.list):
        file = next(element for element in root.list if element.name == request.args.get('name'))
        if request.args.get('directory'):
            file.move_log_file(root)
            return jsonify({
                'message': "Moved successfully.",
                'file': {
                    'directory': file.directory.name,
                    'name': file.name,
                    'contents': file.contents
                }
            }), 200
        elif request.args.get('append'):
            file.append_line(request.args.get('append'))
            return jsonify({
                'message': "Line appended successfully.",
                'file': {
                    'directory': file.directory.name,
                    'name': file.name,
                    'contents': file.contents
                }
            }), 201
        return jsonify({'message': 'Wrong request.'}), 400
    return jsonify({'message': 'File does not exist.'}), 400


def log_text_file_delete(request):
    if request.args.get('name') not in trash and any(file.name == request.args.get('name') for file in root.list):
        file = next(element for element in root.list if element.name == request.args.get('name'))
        file.delete()
        trash.append(request.args.get('name'))
        return jsonify({'message': "Deleted successfully."}), 200
    return jsonify({'message': 'Deleting failed.'}), 400


@app.route('/logtextfile', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def logtextfile():
    if request.method == 'POST':
        return logTextFilePost(request)
    elif request.method == 'GET':
        return log_text_file_get(request)
    elif request.method == 'PATCH':
        return log_text_file_patch(request)
    else:
        return log_text_file_delete(request)


def buffer_file_post(request):
    if any(element.name == request.args.get('name') for element in root.list):
        return jsonify({'message': 'Such file already exists.'}), 400
    file = BufferFile(request.args.get('name'), root, int(request.args.get('max_size')))
    return jsonify({
        'message': 'Created successfully.',
        'file': {
            'directory': file.directory.name,
            'name': file.name,
            'max_size': file.max_size,
            'contents': file.contents
        }
    }), 201


def buffer_file_get(request):
    if any(file.name == request.args.get('name') for file in root.list):
        file = next(element for element in root.list if element.name == request.args.get('name'))
        return jsonify({
            'message': 'Read successfully.',
            'file': {
                'directory': file.directory.name,
                'name': file.name,
                'max_size': file.max_size,
                'contents': file.contents,
            }
        }), 200
    return jsonify({'message': 'Such file does not exist.'}), 400


def buffer_file_patch(request):
    if any(file.name == request.args.get('name') for file in root.list):
        file = next(element for element in root.list if element.name == request.args.get('name'))
        if request.args.get('directory'):
            file.move_buffer_file(root)
            return jsonify({
                'message': 'Moved successfully.',
                'file': {
                    'directory': file.directory.name,
                    'name': file.name,
                    'max_size': file.max_size,
                    'contents': file.contents,
                }
            }), 200
        if request.args.get('push'):
            file.push_element(request.args.get('push'))
            return jsonify({
                'message': 'Element pushed successfully.',
                'file': {
                    'directory': file.directory.name,
                    'name': file.name,
                    'max_size': file.max_size,
                    'contents': file.contents,
                }
            }), 201
        if request.args.get('consume'):
            if len(file.contents) > 0:
                file.consume_element(request.args.get('consume'))
                return jsonify({
                    'message': 'Element consumed successfully.',
                    'file': {
                        'directory': file.directory.name,
                        'name': file.name,
                        'max_size': file.max_size,
                        'contents': file.contents,
                    }
                }), 200
        return jsonify({'message': 'Wrong request.'}), 400
    return jsonify({'message': 'Such file does not exist.'}), 400


def buffer_file_delete(request):
    if request.args.get('name') not in trash and any(file.name == request.args.get('name') for file in root.list):
        file = next(element for element in root.list if element.name == request.args.get('name'))
        file.delete()
        trash.append(request.args.get('name'))
        return jsonify({'message': 'Deleted successfully.'}), 200
    return jsonify({'message': 'Deleting failed.'}), 400


@app.route('/bufferfile', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def bufferfile():
    if request.method == 'POST':
        return buffer_file_post(request)
    elif request.method == 'GET':
        return buffer_file_get(request)
    elif request.method == 'PATCH':
        return buffer_file_patch(request)
    else:
        return buffer_file_delete(request)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
