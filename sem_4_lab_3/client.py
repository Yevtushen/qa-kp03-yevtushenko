from flask import Flask
import requests
import click

app = Flask(__name__)


@click.group()
def cli():
    pass


@click.command(name="create_directory")
@click.argument('parent_directory')
@click.argument('name')
@click.argument('max_size')
def create_directory(parent_directory, name, max_size):
    for_post = {
        'parent_directory': parent_directory,
        'name' : name,
        'max_size' : max_size
    }
    response = requests.post("http://127.0.0.1:5000/directory", params=for_post)
    print(response)


@click.command(name="delete_directory")
@click.argument('name')
def delete_directory(name):
    for_delete = {'name': name}
    response = requests.delete("http://127.0.0.1:5000/directory", params=for_delete)
    print(response)


@click.command(name="list_directory")
@click.argument('parent_directory')
@click.argument('name')
@click.argument('max_size')
def list_directory(name, parent_directory, max_size):
    for_get = {
        'parent_directory': parent_directory,
        'name': name,
        'max_size': max_size
    }
    response = requests.get("http://127.0.0.1:5000/directory", params=for_get)
    print(response)


@click.command(name="move_directory")
@click.argument('parent_directory')
@click.argument('name')
@click.argument('max_size')
def move_directory(parent_directory, name, max_size):
    for_patch = {
        'parent_directory': parent_directory,
        'name': name,
        'max_size': max_size
    }
    response = requests.patch("http://127.0.0.1:5000/directory", params=for_patch)
    print(response)
    pass


@click.command(name="create_binary_file")
@click.argument('directory')
@click.argument('name')
@click.argument('contents')
def create_binary_file(directory, name, contents):
    for_post = {
        'directory': directory,
        'name': name,
        'contents': contents
    }
    response = requests.post("http://127.0.0.1:5000/binaryfile", params=for_post)
    print(response)


@click.command(name="delete_binary_file")
@click.argument('name')
def delete_binary_file(name):
    for_delete = {'name': name}
    response = requests.delete("http://127.0.0.1:5000/binaryfile", params=for_delete)
    print(response)


@click.command(name="move_binary_file")
@click.argument('directory')
@click.argument('name')
@click.argument('contents')
def move_binary_file(directory, name, contents):
    for_patch = {
        'directory': directory,
        'name': name,
        'contents': contents
    }
    response = requests.patch("http://127.0.0.1:5000/binaryfile", params=for_patch)
    print(response)


@click.command(name="read_binary_file")
@click.argument('directory')
@click.argument('name')
@click.argument('contents')
def read_binary_file(directory, name, contents):
    for_get = {
        'directory': directory,
        'name': name,
        'contents': contents
    }
    response = requests.get("http://127.0.0.1:5000/binaryfile", params=for_get)
    print(response)


@click.command(name="create_buffer_file")
@click.argument('directory')
@click.argument('name')
@click.argument('max_size')
@click.argument('contents')
def create_buffer_file(directory, name, max_size, contents):
    for_post = {
        'directory': directory,
        'name': name,
        'max_size': max_size,
        'contents': contents
    }
    response = requests.post("http://127.0.0.1:5000/bufferfile", params=for_post)
    print(response)


@click.command(name="delete_buffer_file")
@click.argument('name')
def delete_buffer_file(name):
    for_delete = {'name': name}
    response = requests.post("http://127.0.0.1:5000/bufferfile", params=for_delete)
    print(response)


@click.command(name="move_buffer_file")
@click.argument('directory')
@click.argument('name')
@click.argument('max_size')
@click.argument('contents')
def move_buffer_file(directory, name, max_size, contents):
    for_patch = {
        'directory': directory,
        'name': name,
        'max_size' : max_size,
        'contents': contents
    }
    response = requests.patch("http://127.0.0.1:5000/bufferfile", params=for_patch)
    print(response)


@click.command(name="read_buffer_file")
@click.argument('directory')
@click.argument('name')
@click.argument('max_size')
@click.argument('contents')
def read_buffer_file(directory, name, max_size, contents):
    for_get = {
        'directory': directory,
        'name': name,
        'max_size' : max_size,
        'contents': contents
    }
    response = requests.get("http://127.0.0.1:5000/bufferfile", params=for_get)
    print(response)


@click.command(name="push_buffer_file")
@click.argument('name')
@click.argument('element')
def push_buffer_file(name, element):
    for_patch = {
        'name' : name,
        'push' : element
    }
    response = requests.patch("http://127.0.0.1:5000/bufferfile", params=for_patch)
    print(response)


@click.command(name="consume_buffer_file")
@click.argument('name')
@click.argument('element')
def consume_buffer_file(name, element):
    for_patch = {
        'name': name,
        'consume': element,
    }
    response = requests.patch("http://127.0.0.1:5000/bufferfile", params=for_patch)
    print(response)


@click.command(name="create_log_text_file")
@click.argument('directory')
@click.argument('name')
@click.argument('contents')
def create_log_text_file(directory, name, contents):
    for_post = {
        'directory': directory,
        'name': name,
        'contents': contents
    }
    response = requests.post("http://127.0.0.1:5000/logtextfile", params=for_post)
    print(response)


@click.command(name="delete_log_text_file")
@click.argument('name')
def delete_log_text_file(name):
    for_delete = {'name': name}
    response = requests.delete("http://127.0.0.1:5000/logtextfile", params=for_delete)
    print(response)


@click.command(name="move_log_text_file")
@click.argument('directory')
@click.argument('name')
@click.argument('contents')
def move_log_text_file(directory, name, contents):
    for_patch = {
        'directory': directory,
        'name': name,
        'contents': contents
    }
    response = requests.patch("http://127.0.0.1:5000/bufferfile", params=for_patch)
    print(response.content)


@click.command(name="read_log_text_file")
@click.argument('directory')
@click.argument('name')
@click.argument('contents')
def read_log_text_file(directory, name, contents):
    for_get = {
        'directory': directory,
        'name': name,
        'contents': contents
    }
    response = requests.get("http://127.0.0.1:5000/logtextfile", params=for_get)
    print(response)


@click.command(name="append_log_text_file")
@click.argument('name')
@click.argument('append')
def append_log_text_file(name, line):
    for_patch = {
        'name' : name,
        'append' : line
    }
    response = requests.patch("http://127.0.0.1:5000/logtextfile", params=for_patch)
    print(response)


cli.add_command(create_directory)
cli.add_command(delete_directory)
cli.add_command(move_directory)
cli.add_command(list_directory)

cli.add_command(create_binary_file)
cli.add_command(delete_binary_file)
cli.add_command(move_binary_file)
cli.add_command(read_binary_file)

cli.add_command(create_buffer_file)
cli.add_command(delete_buffer_file)
cli.add_command(move_buffer_file)
cli.add_command(push_buffer_file)
cli.add_command(consume_buffer_file)

cli.add_command(create_log_text_file)
cli.add_command(delete_log_text_file)
cli.add_command(move_log_text_file)
cli.add_command(read_log_text_file)
cli.add_command(append_log_text_file)


if __name__ == '__main__':
    cli()
