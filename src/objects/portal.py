from src.common.exec_interrupt import MapExit
from src.common.point import Point
from src.objects.object import Object


class Portal(Object):
    """
    `Object` allowing the player to move to a next `scene`.
    """

    def __init__(self, scene: 'Scene', position: Point = Point(0, 0)) -> None:
        super().__init__(position, scene)
        self.walkable = True

    def on_collision(self, other) -> None:
        self.scene.runtime.next_scene.execute()
        # Stop execution flow of `exec`
        raise MapExit
