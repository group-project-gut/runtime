import pytest

from src.runtime import Runtime


def test_move_and_direction_success():
    code = '''
move(Direction.NORTH)
move(Direction.EAST)
move(Direction.SOUTH)
move(Direction.WEST)'''
    runtime = Runtime(code, False)
    runtime.run()


def test_len_success():
    code = '''a = len([1, 2, 3])'''
    runtime = Runtime(code, False)
    runtime.run()


def test_range_success():
    code = '''
for _ in range(3):
    pass
'''
    runtime = Runtime(code, False)
    runtime.run()


def test_enumerate_success():
    code = '''
for _ in enumerate(['a', 'b', 'c']):
    pass
'''
    runtime = Runtime(code, False)
    runtime.run()


def test_import_failure():
    code = '''import os'''
    runtime = Runtime(code, False)
    with pytest.raises(ImportError):
        runtime.run()


def test_open_failure():
    code = '''open('test.txt')'''
    runtime = Runtime(code, False)
    with pytest.raises(NameError):
        runtime.run()


def test_print_failure():
    code = '''print('test')'''
    runtime = Runtime(code, False)
    with pytest.raises(NameError):
        runtime.run()
