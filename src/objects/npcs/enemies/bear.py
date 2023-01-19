from transitions import Machine

from src.common.enums import Direction
from src.objects.npcs.enemy import Enemy
from src.common.point import Point
from src.actions.prepare_to_slam import PrepareToSlam
from src.actions.attacks.slam import Slam

HP = 100
STATES = ['idle', 'move', 'prepare_to_slam', 'slam']
TRANSITIONS = [{'trigger': 'idle2prepare_to_slam', 'source': 'idle', 'dest': 'prepare_to_slam', 'conditions': 'idle2prepare_to_slam_condition'},
               {'trigger': 'idle2move', 'source': 'idle', 'dest': 'move', 'conditions': 'idle2move_condition'},
               {'trigger': 'move2prepare_to_slam', 'source': 'move', 'dest': 'prepare_to_slam', 'conditions': 'move2prepare_to_slam_condition'},
               {'trigger': 'move2idle', 'source': 'move', 'dest': 'idle', 'conditions': 'move2idle_condition'},
               {'trigger': 'prepare_to_slam2slam', 'source': 'prepare_to_slam', 'dest': 'slam'},
               {'trigger': 'slam2idle', 'source': 'slam', 'dest': 'idle'}]


class Bear(Enemy):
    """
    Bear boss.
    """

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(scene, position, HP,
                         Machine(model=self, states=STATES, transitions=TRANSITIONS, initial='idle'))

    def tick(self) -> None:
        self.machine.on_enter_idle(self.idle())
        self.machine.on_enter_move(self.move())
        self.machine.on_enter_prepare_to_slam(self.prepare_to_slam())
        self.machine.on_enter_slam(self.slam())

    def slam(self):
        Slam(self, [self.properties.position + Direction.NORTH.value,
                    self.properties.position + Direction.WEST.value,
                    self.properties.position + Direction.SOUTH.value,
                    self.properties.position + Direction.EAST.value]).execute()

    def prepare_to_slam(self):
        PrepareToSlam(self).execute()

    def idle2prepare_to_slam_condition() -> bool:
        return True

    def idle2move_condition() -> bool:
        return True

    def move2prepare_to_slam_condition() -> bool:
        return True

    def move2idle_condition() -> bool:
        return True
