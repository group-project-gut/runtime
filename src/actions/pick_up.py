from src.actions.action import Action
from src.objects.interactive_object import InteractiveObject


class PickUp(Action):
    """
    Action for picking up interactive objects
    """

    def __init__(self, agent: 'Agent', object_id: int) -> None:
        super().__init__()
        self.properties.object_id = object_id
        self.properties.agent_id = agent.properties.id
        self.agent = agent

    def execute(self) -> None:
        target_object = self.agent.scene.get_object_by_id(self.properties.object_id)
        if not self.__can_pick_up(target_object):
            # log here: print(f"Unable to pick up object with id {self.object_id}")
            return

        self.log()
        self.agent.scene.remove_object_from_id_map(target_object)
        self.agent.add_item_to_equipment(target_object)

    def __can_pick_up(self, target_object):
        if (target_object.properties.position.__eq__(self.agent.properties.position) and
                isinstance(target_object, InteractiveObject) and
                target_object.can_pick_up):
            return True

        return False
