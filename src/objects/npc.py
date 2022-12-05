import random

from transitions import Machine, State

from src.common.point import Point
from src.objects.object import Object
from src.common.serializable import Properties
from src.actions.move import Move
from src.actions.idle import Idle
from src.common.enums import Direction


class NPC(Object):
    """
    Simple agent existing in a `scene`.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool
    machine: Machine

    states = [State(name='idle', on_enter=['idle']), State(name='moving', on_enter=['move'])]

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(position, scene)
        self.machine = Machine(model=self, states=NPC.states, initial='idle')
        self.machine.add_ordered_transitions(loop=True)

    def move(self):
        Move(self, random.choice(list(Direction))).execute()

    def idle(self):
        Idle(self).execute()

    def tick(self) -> None:
        """
        Called on an `Object`, so it can perform some actions
        """
        self.next_state()
