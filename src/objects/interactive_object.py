from src.common.point import Point
from src.objects.object import Object


class InteractiveObject(Object):
    """
    Abstract represents object that can interact with each other
    """
    can_pick_up: bool

    def __init__(self, position: Point, scene: 'Scene') -> None:
        super().__init__(position, scene)
