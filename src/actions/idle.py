from src.actions.action import Action
from src.common.serializable import Properties
from src.objects.object import Object


class Idle(Action):
    """
    Simple action for idling.
    """
    base: str
    properties: Properties
    object: Object

    def __init__(self, object: Object) -> None:
        super().__init__()
        self.properties.object_id = object.properties.id
        self.object = object

    def execute(self) -> None:
        self.log()
