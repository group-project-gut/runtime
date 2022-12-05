import random

from transitions import Machine, State

from src.common.point import Point
from src.objects.object import Object
from src.common.serializable import Properties


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
        neighboring_points = [self.properties.position + Point(1, 0), self.properties.position + Point(-1, 0),
                              self.properties.position + Point(0, 1),
                              self.properties.position + Point(0, -1)]
        walkable_fields = [point for point in neighboring_points if self.scene.is_walkable_field(point)]
        if walkable_fields:
            self.scene.move_object(self, random.choice(walkable_fields))

    def idle(self):
        pass

    def tick(self) -> None:
        """
        Called on an `Object`, so it can perform some actions
        """
        self.next_state()
