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
        super().__init__(scene, position, HP, BearStateMachine(self))

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


class BearStateMachine(StateMachine):
    def __init__(self, bear: Bear):
        super().__init__()
        self.bear = bear
        self.add_state("idle")\
            .add_state("move")\
            .add_state("prepare_to_slam")\
            .add_state("slam")\
            .add_transition("idle", "prepare_to_slam", lambda: self.bear.is_there_agent_to_slam())\
            .add_transition("idle", "move", lambda: True)\
            .add_transition("move", "prepare_to_slam", lambda: self.bear.is_there_agent_to_slam())\
            .add_transition("prepare_to_slam", "slam", lambda: True)\
            .add_transition("slam", "idle", lambda: True)\
            .set_state("idle")

    def _state_logic(self):
        match self._state:
            case "idle":
                self.bear.idle()
            case "move":
                self.bear.move()
            case "prepare_to_slam":
                self.bear.prepare_to_slam()
            case "slam":
                self.bear.slam()

    def _enter_state(self, new_state, old_state):
        pass

    def _exit_state(self, old_state, new_state):
        pass
