from typing import Dict

from src.actions.action import Action
from src.actions.destroy import Destroy
from src.common.point import Point
from src.common.serializable import Properties
from src.objects.interactive_object import InteractiveObject
from src.objects.object import Object


class PickUp(Action):
    """
    Action for picking up interactive objects
    """
    base: str
    properties: Properties
    agent: 'Agent'
    objects_dict: Dict[int, Object]
    agent_position: Point
    object_id: int  # id of the object being picked up

    def __init__(self, agent: 'Agent', object_id: int) -> None:
        super().__init__()
        self.properties.object_id = object_id
        self.properties.agent = agent.properties.id
        self.agent = agent

    def execute(self) -> None:
        self.__pick_up()

    def __pick_up(self):
        target_object = self.objects_dict.get(self.object_id)
        if not self.__can_pick_up(target_object):
            # log here: print(f"Unable to pick up object with id {self.object_id}")
            return

        self.log()
        self.agent.items.append(target_object.properties.id)
        self.agent.scene.objects_map[target_object.properties.position].remove(target_object)

    def __can_pick_up(self, raised_object):
        if (raised_object.properties.position.__eq__(self.agent_position) and
                issubclass(raised_object.__class__, InteractiveObject) and
                raised_object.can_pick_up):
            return True

        return False
