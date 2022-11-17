import operator

from src.scene import Scene

from .object import Object
from src.common.enums import Direction
from src.common.point import Point


class Agent(Object):
    def __init__(self, scene: Scene,position: Point = Point(0, 0)):
        super().__init__(position, scene)
        self.scene.add_object(self)
