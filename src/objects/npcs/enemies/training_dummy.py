from transitions import State

from src.objects.npcs.enemy import Enemy
from src.common.point import Point
from src.common.serializable import Properties

TRAINING_DUMMY_HP = 1000000
TRAINING_DUMMY_STATES = [State(name='idle', on_enter=['idle'])]


class TrainingDummy(Enemy):
    """
    Enemy that does not do anything.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(scene, position, TRAINING_DUMMY_HP, TRAINING_DUMMY_STATES)
