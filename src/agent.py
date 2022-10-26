import operator
from .enums import Direction

class Agent:
    position: tuple[int, int]

    def __init__(self, position: tuple[int, int]):
        self.position = (0, 0)

    def move(self, dir: Direction):
        print(f"MOVE {str(dir)}")
        self.position = tuple(map(operator.add, self.position, dir.value))

    def __str__(self) -> str:
        return f"AGENT ({self.position[0]}, {self.position[1]})"