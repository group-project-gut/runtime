from typing import List

from src.common.point import Point
from src.actions.action import Action
from src.actions.deal_dmg import DealDmg
from src.objects.object import Object
from src.objects.npc import NPC
from src.objects.agent import Agent

SLAM_DMG = 10


class Slam(Action):
    """
    Simple action for attacking.
    """
    object: Object

    def __init__(self, object: Object, points: List[Point]) -> None:
        super().__init__()
        self.properties.object_id = object.properties.id
        self.object = object
        self.properties.points = points

    def execute(self) -> None:
        self.log()
        for target_position in self.properties.points:
            if not self.object.scene._objects_position_map.get(target_position):
                continue
            for target in self.object.scene.get_objects_by_position(target_position):
                if isinstance(target, NPC) or isinstance(target, Agent):
                    DealDmg(target, SLAM_DMG).execute()
