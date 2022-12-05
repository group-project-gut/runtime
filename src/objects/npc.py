import random

from statemachine import StateMachine, State

from src.common.point import Point
from src.objects.object import Object
from src.common.serializable import Properties


class NPC(Object, StateMachine):
    """
    Simple agent existing in a `scene`.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool

    idle_state = State('Idle', initial=True)
    move_state = State('Move')
    cycle = idle_state.to(move_state) | move_state.to(idle_state)

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(position, scene)

    def on_enter_move(self):
        neighboring_points = [self.position + Point(1, 0), self.position - Point(1, 0), self.position + Point(0, 1),
                              self.position - Point(0, 1)]
        walkable_fields = [point for point in neighboring_points if self.scene.is_walkable_field(point)]
        if walkable_fields:
            self.scene.move_object(random.choice(walkable_fields))

    def on_enter_idle(self):
        pass

    def tick(self) -> None:
        """
        Called on an `Object`, so it can perform some actions
        """
        self.cycle()
