import operator

from .enums import Direction


class Agent:
    position: tuple[int, int]

    def __init__(self, position=(0, 0)) -> None:
        self.position = position

    def move(self, direction: Direction) -> None:
        print(f"MOVE {str(direction)}")
        self.position = tuple(map(operator.add, self.position, direction.value))

    def __str__(self) -> str:
        return f"AGENT ({self.position[0]}, {self.position[1]})"
