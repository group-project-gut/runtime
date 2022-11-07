import math


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    # xxxXXXxxx WAAAAAAAAAARRRRRNINGGGGGGGG xxxXXXxxx
    # Position is passed to properties as string,
    # so frontends MUST parse the string on their own.
    # It's not another JSON dictionary for reasons.
    # That is - C# casting magic :)
    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def dist_to(self, point) -> float:
        dist: float = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return dist
