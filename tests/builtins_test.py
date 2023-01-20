import pytest
from tests.helpers.utils import create_code_file

from src.runtime import Runtime


def test_move_and_direction_success():
    code = '''
move(Direction.NORTH)
move(Direction.EAST)
move(Direction.SOUTH)
move(Direction.WEST)'''

    path = create_code_file(code)

    runtime = Runtime(path, False)
    runtime.run()


def test_len_success():
    code = '''a = len([1, 2, 3])'''
    path = create_code_file(code)
    runtime = Runtime(path, False)
    runtime.run()


def test_range_success():
    code = '''
for _ in range(3):
    pass
'''
    path = create_code_file(code)
    runtime = Runtime(path, False)
    runtime.run()


def test_enumerate_success():
    code = '''
for _ in enumerate(['a', 'b', 'c']):
    pass
'''
    path = create_code_file(code)
    runtime = Runtime(path, False)
    runtime.run()


def test_import_failure():
    code = '''import os'''
    path = create_code_file(code)
    runtime = Runtime(path, False)
    with pytest.raises(ImportError):
        runtime.run()


def test_open_failure():
    code = '''open('test.txt')'''
    path = create_code_file(code)
    runtime = Runtime(path, False)
    with pytest.raises(NameError):
        runtime.run()


def test_print_failure():
    code = '''print('test')'''
    path = create_code_file(code)
    runtime = Runtime(path, False)
    with pytest.raises(NameError):
        runtime.run()
