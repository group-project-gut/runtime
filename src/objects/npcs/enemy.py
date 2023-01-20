from src.common.state_machine import StateMachine
from src.objects.npc import NPC
from src.common.point import Point


class Enemy(NPC):
    """
    Enemy interface.
    """

    def __init__(self, scene: 'Scene', position: Point, hp: int, machine: StateMachine) -> None:
        super().__init__(scene, position, hp, machine)
