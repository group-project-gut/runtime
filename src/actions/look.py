from typing import List
from src.common.enums import Direction
from src.common.point import Point
from src.actions.action import Action
from src.common.serializable import Properties
from src.objects.object import Object


class Look(Action):
    """
    Simple looking action. Returns list of objects in set direction.
    """
    base: str
    properties: Properties
    object: Object

    def __init__(self, object: Object, direction: Direction) -> None:
        super().__init__()
        self.properties.object_id = object.properties.id
        self.object = object
        self.properties.direction = direction

    def execute(self) -> List[Object]:
        self.log()
        target_position: Point = self.object.properties.position + self.properties.direction.value
        return [target.name for target in self.object.scene.get_objects_by_position(target_position)]
