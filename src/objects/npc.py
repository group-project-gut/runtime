import random

from transitions import Machine

from src.common.point import Point
from src.objects.object import Object
from src.common.serializable import Properties
from src.actions.move import Move
from src.actions.idle import Idle
from src.common.enums import Direction


class NPC(Object):
    """
    NPC interface.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool
    machine: Machine
    hp: int

    def __init__(self, scene: 'Scene', position: Point, hp: int, machine: Machine) -> None:
        super().__init__(position, scene)
        self.machine = machine
        self.hp = hp

    def move(self):
        Move(self, random.choice(list(Direction))).execute()

    def idle(self):
        Idle(self).execute()
