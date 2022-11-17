from .object import Object
from src.common.enums import Direction
from src.common.point import Point


class Portal(Object):
    def __init__(self, scene, position: Point = Point(0, 0)) -> None:
        super().__init__(position, scene)
        self.walkable = True

    def on_collision(self, other) -> None:
        self.scene.create.execute(self.scene)
        return super().on_collision(other)
