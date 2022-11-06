from src.runtime import Runtime


def test_move_and_direction_success():
    code = '''
move(Direction.UP)
move(Direction.RIGHT)
move(Direction.DOWN)
move(Direction.LEFT)'''
    runtime = Runtime(code)
    runtime.run()


def test_len_success():
    code = '''
a = len([1, 2, 3])'''
    runtime = Runtime(code)
    runtime.run()


def test_range_success():
    code = '''
for _ in range(3):
    pass'''
    runtime = Runtime(code)
    runtime.run()


def test_enumerate_success():
    code = '''
for _ in enumerate(['a', 'b', 'c']):
    pass'''
    runtime = Runtime(code)
    runtime.run()
