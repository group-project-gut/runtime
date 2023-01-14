from src.common.exec_interrupt import MapExit
from src.objects.npc import NPC
from src.common.point import Point
from src.common.serializable import Properties


class Enemy(NPC):
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool

    def __init__(self, scene: 'Scene', position: Point, hp: int) -> None:
        super().__init__(scene, position, hp)

    def on_collision(self, other) -> None:
        self.scene.runtime.next_scene.execute()
        # Stop execution flow of `exec`
        raise MapExit
