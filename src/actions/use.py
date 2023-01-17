from src.actions.action import Action
from src.common.point import Point
from src.common.serializable import Properties
from src.objects.interactive_object import InteractiveObject


class Use(Action):
    """
    An action that provides the opportunity to interact with another object
    """
    base: str
    properties: Properties
    agent: 'Agent'
    object_id: int  # object id for interaction
    range: int

    def __init__(self, agent: 'Agent', object_id: int, scope_of_interaction: int = 1) -> None:
        super().__init__()
        self.properties.agent = agent
        self.properties.object_id = object_id
        self.properties.range = scope_of_interaction

    def execute(self) -> None:
        interactive_object = self.agent.scene.objects_dict.get(self.object_id)
        if not self.can_interact(interactive_object):
            # log here
            return

        interactive_object.interact(self.agent)

    def can_interact(self, interactive_object: InteractiveObject):
        if not issubclass(interactive_object.__class__, InteractiveObject):
            return False

        agent_position = self.agent.properties.position
        interactive_object_position = interactive_object.properties.position
        for i in range(-self.range, self.range + 1):
            for j in range(-self.range, self.range + 1):
                if interactive_object_position.__eq__(agent_position.__add__(Point(i, j))):
                    return True

        return False
