from src.common.point import Point
from .object import Object


class Agent(Object):
    '''
    Simple agent existing in a `scene`.
    '''
    def __init__(self, scene, position: Point = Point(0, 0)):
        super().__init__(position, scene)
