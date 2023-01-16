from src.common.point import Point
from src.common.serializable import Properties
from src.objects.agent import Agent
from src.objects.interactive_object import InteractiveObject


class Door(InteractiveObject):
    """
    `Object` interacting with a key
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool
    keys: list

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(position, scene)
        self.keys = []
        self.can_pick_up = False

    def interact(self, object_triggering_interact) -> None:
        if isinstance(object_triggering_interact, Agent) and self.can_open(object_triggering_interact.items):
            print("Opening door!")

    def can_open(self, items: list):
        return any(item in self.keys for item in items)
