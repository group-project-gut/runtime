from typing import Union


from src.actions.action import Action
from src.common.serializable import Properties
from src.objects.npc import NPC


class Destroy(Action):
    """
    Simple action for dying.
    """
    object: Union['Agent', NPC]

    def __init__(self, object: Union['Agent', NPC]) -> None:
        super().__init__()
        self.properties.object_id = object.properties.id
        self.object = object

    def execute(self) -> None:
        self.object.free_field(self.object.properties.position)
        self.object.scene.remove_object_from_id_map(self.object)
        self.log()
