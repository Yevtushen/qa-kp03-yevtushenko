from flask import Flask, request
import requests
import click

app = Flask(__name__)


@click.command(name="create_directory")
@click.argument('name')
@click.argument('parent_directory')
@click.argument('max_size')
def create_directory():
    pass


@click.command(name="delete_directory")
@click.argument('name')
@click.argument('parent_directory')
@click.argument('max_size')
def delete_directory():
    pass


@click.command(name="list_directory")
@click.argument('name')
@click.argument('parent_directory')
@click.argument('max_size')
def list_directory():
    pass


@click.command(name="move_directory")
@click.argument('name')
@click.argument('parent_directory')
@click.argument('max_size')
def move_directory():
    pass


@click.command(name="create_binary_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def create_binary_file():
    pass


@click.command(name="delete_binary_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def delete_binary_file():
    pass

@click.command(name="move_binary_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def move_binary_file():
    pass


@click.command(name="read_binary_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def read_binary_file():
    pass

@click.command(name="create_buffer_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def create_buffer_file():
    pass


@click.command(name="delete_buffer_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def delete_buffer_file():
    pass

@click.command(name="move_buffer_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def move_buffer_file():
    pass

@click.command(name="push_buffer_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
@click.argument('element')
def push_buffer_file():
    pass

@click.command(name="create_buffer_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
@click.argument('element')
def pull_buffer_file():
    pass


@click.command(name="create_log_text_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def create_log_text_file():
    pass


@click.command(name="delete_log_text_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def delete_log_text_file():
    pass


@click.command(name="move_log_text_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def move_log_text_file():
    pass


@click.command(name="read_log_text_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
def read_log_text_file():
    pass


@click.command(name="append_log_text_file")
@click.argument('name')
@click.argument('directory')
@click.argument('contents')
@click.argument('line')
def append_log_text_file():
    pass