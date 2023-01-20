from src.common.enums import Direction
from src.common.point import Point
from src.actions.action import Action
from src.actions.deal_dmg import DealDmg
from src.objects.object import Object
from src.objects.npcs.enemy import Enemy

SLASH_DMG = 100


class Slash(Action):
    """
    Simple action for attacking.
    """
    object: Object

    def __init__(self, object: Object, direction: Direction) -> None:
        super().__init__()
        self.properties.object_id = object.properties.id
        self.object = object
        self.properties.direction = direction

    def execute(self) -> None:
        self.log()
        target_position: Point = self.object.properties.position + self.properties.direction.value
        for target in self.object.scene.get_objects_by_position(target_position):
            if isinstance(target, Enemy):
                DealDmg(target, 100).execute()
