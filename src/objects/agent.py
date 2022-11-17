import operator

from .object import Object
from src.common.enums import Direction
from src.common.point import Point


class Agent(Object):
    def __init__(self, scene, position: Point = Point(0, 0)):
        super().__init__(position, scene)
