from enum import Enum

class Direction(Enum):
    UP = (0, 1)
    RIGHT = (1, 0)
    DOWN = (0, -1)
    LEFT = (-1, 0)

    def __str__(self):
        if self == Direction.UP:
            return "UP"
        elif self == Direction.RIGHT:
            return "RIGHT"
        elif self == Direction.RIGHT:
            return "DOWN"
        elif self == Direction.RIGHT:
            return "LEFT"