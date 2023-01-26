from src.actions.action import Action
from src.common.enums import Direction
from src.objects.door import Door
from src.objects.object import Object


class OpenDoor(Action):

    def __init__(self, object: Object, direction: Direction) -> None:
        super().__init__()
        self.properties.object_id = object.properties.id
        self.object = object
        self.properties.direction = direction

    def execute(self) -> None:
        target_position = self.object.properties.position + self.properties.direction.value
        for target in self.object.scene.get_objects_by_position(target_position):
            if isinstance(target, Door):
                target.try_open(self.object)
