from src.common.state_machine import StateMachine
from src.objects.npc import NPC
from src.common.point import Point
from src.common.serializable import Properties


class Enemy(NPC):
    """
    Enemy interface.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool
    machine: StateMachine
    hp: int

    def __init__(self, scene: 'Scene', position: Point, hp: int, machine: StateMachine) -> None:
        super().__init__(scene, position, hp, machine)
