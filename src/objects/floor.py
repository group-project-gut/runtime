from src.common.point import Point
from src.objects.object import Object
from src.common.serializable import Properties


class Floor(Object):
    """
    Simple walkable `Object`.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool

    def __init__(self, scene: 'Scene', position: Point = Point(0, 0)) -> None:
        super().__init__(position, scene)
        self.walkable = True
