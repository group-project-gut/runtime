from .object import Object
from src.common.enums import Direction
from src.common.point import Point


class Floor(Object):
    '''
    Simple walkable `Object`.
    '''
    def __init__(self, scene, position: Point = Point(0, 0)) -> None:
        super().__init__(position, scene)
        self.walkable = True
