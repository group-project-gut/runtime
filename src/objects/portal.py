from src.common.exec_interrupt import ExecInterrupt
from src.common.point import Point
from .object import Object


class Portal(Object):
    '''
    `Object` allowing the player to move to a next `scene`.
    '''

    def __init__(self, scene, position: Point = Point(0, 0)) -> None:
        super().__init__(position, scene)
        self.walkable = True

    def on_collision(self, other) -> None:
        self.scene.runtime.next_scene.execute()
        # Stop execution flow of `exec`
        raise ExecInterrupt
