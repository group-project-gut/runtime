import math

class Point:
    def __init__(self, x, y) -> None:
        self.x: int = x
        self.y: int = y

    def __str__(self) -> str:
        return f"{{\"x\" : {self.x}, \"y\" : {self.y}}}"

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def dist_to(self, point) -> float:
        dist: float = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return dist