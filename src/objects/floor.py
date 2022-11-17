from src.scene import Scene
from .object import Object
from src.common.enums import Direction
from src.common.point import Point

class Floor(Object):
    def __init__(self, scene: Scene, position: Point = Point(0, 0)) -> None:
        super().__init__(position, scene)
        self.walkable = True