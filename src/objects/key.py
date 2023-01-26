from src.common.point import Point
from src.objects.interactive_object import InteractiveObject


class Key(InteractiveObject):
    """
    `Object` existing in a `scene`.
    """

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(position, scene)
        self.can_pick_up = True

    def on_collision(self, other) -> None:
        pass
