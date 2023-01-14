from src.common.enums import Direction
from src.common.point import Point
from src.actions.action import Action
from src.actions.deal_damage import DealDamage
from src.common.serializable import Properties
from src.objects.object import Object


class Slash(Action):
    """
    Simple action for attacking.
    """
    base: str
    properties: Properties
    object: Object

    def __init__(self, object: Object, direction: Direction) -> None:
        super().__init__()
        self.properties.object_id = object.properties.id
        self.object = object
        self.properties.direction = direction

    def execute(self) -> None:
        self.log()
        enemy_position: Point = self.object.properties.position + self.properties.direction.value
        if enemy := self.object.scene[enemy_position]:
            DealDamage(enemy, 100).execute()
