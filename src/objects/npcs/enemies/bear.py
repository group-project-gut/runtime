from typing import List
from enum import Enum

from src.common.state_machine import StateMachine
from src.common.enums import Direction
from src.objects.npcs.enemy import Enemy
from src.objects.agent import Agent
from src.common.point import Point
from src.actions.prepare_to_slam import PrepareToSlam
from src.actions.attacks.slam import Slam

HP = 100


class Bear(Enemy):
    """
    Bear boss.
    """

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(scene, position, HP, Bear.BearStateMachine(self))

    def occupied_fields(self, current_position: Point = None) -> List[Point]:
        if not current_position:
            current_position = self.properties.position
        return [current_position,
                current_position + Point(0, 1),
                current_position + Point(1, 1),
                current_position + Point(1, 0)]

    def tick(self) -> None:
        self.machine.tick()

    def slam(self):
        Slam(self, [self.properties.position + Direction.NORTH.value,
                    self.properties.position + Direction.WEST.value,
                    self.properties.position + Direction.SOUTH.value,
                    self.properties.position + Direction.EAST.value]).execute()

    def prepare_to_slam(self):
        PrepareToSlam(self).execute()

    def is_there_agent_to_slam(self):
        points_around = [self.properties.position + Direction.NORTH.value,
                         self.properties.position + Direction.WEST.value,
                         self.properties.position + Direction.SOUTH.value,
                         self.properties.position + Direction.EAST.value]
        for target_position in points_around:
            if not self.scene._objects_position_map.get(target_position):
                continue
            for target in self.scene.get_objects_by_position(target_position):
                if isinstance(target, Agent):
                    return True
        return False

    class State(Enum):
        IDLE = 0
        MOVE = 1
        PREPARE_TO_SLAM = 2
        SLAM = 3

    class BearStateMachine(StateMachine):

        def __init__(self, bear: 'Bear'):
            super().__init__()
            self.bear = bear
            self.add_state(Bear.State.IDLE)\
                .add_state(Bear.State.MOVE)\
                .add_state(Bear.State.PREPARE_TO_SLAM)\
                .add_state(Bear.State.SLAM)\
                .add_transition(Bear.State.IDLE, Bear.State.PREPARE_TO_SLAM, lambda: self.bear.is_there_agent_to_slam())\
                .add_transition(Bear.State.IDLE, Bear.State.MOVE, lambda: True)\
                .add_transition(Bear.State.MOVE, Bear.State.PREPARE_TO_SLAM, lambda: self.bear.is_there_agent_to_slam())\
                .add_transition(Bear.State.PREPARE_TO_SLAM, Bear.State.SLAM, lambda: True)\
                .add_transition(Bear.State.SLAM, Bear.State.IDLE, lambda: True)\
                .set_state(Bear.State.IDLE)

        def _state_logic(self):
            match self._state:
                case Bear.State.IDLE:
                    self.bear.idle()
                case Bear.State.MOVE:
                    self.bear.move()
                case Bear.State.PREPARE_TO_SLAM:
                    self.bear.prepare_to_slam()
                case Bear.State.SLAM:
                    self.bear.slam()

        def _enter_state(self, new_state, old_state):
            pass

        def _exit_state(self, old_state, new_state):
            pass
