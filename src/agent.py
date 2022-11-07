import operator

from .object import Object
from .enums import Direction
from .point import Point


class Agent(Object):
    def __init__(self, position: Point = Point(0, 0)):
        super().__init__(position)
