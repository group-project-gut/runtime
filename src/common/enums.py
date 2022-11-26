from enum import Enum
from src.common.point import Point


class Direction(Enum):
    """
    Enumeration representing global directions
    """

    UP = Point(0, 1)
    RIGHT = Point(1, 0)
    DOWN = Point(0, -1)
    LEFT = Point(-1, 0)

    def __str__(self) -> str:
        if self == Direction.UP:
            return "UP"
        elif self == Direction.RIGHT:
            return "RIGHT"
        elif self == Direction.DOWN:
            return "DOWN"
        elif self == Direction.LEFT:
            return "LEFT"
