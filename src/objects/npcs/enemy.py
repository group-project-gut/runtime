from transitions import Machine

from src.objects.npc import NPC
from src.common.point import Point


class Enemy(NPC):
    """
    Enemy interface.
    """

    def __init__(self, scene: 'Scene', position: Point, hp: int, machine: Machine) -> None:
        super().__init__(scene, position, hp, machine)
