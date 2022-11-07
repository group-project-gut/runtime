from src.objects.object import Object
from src.objects.agent import Agent
from src.common.serializable import Serializable


class Action(Serializable):
    def __init__(self, agent_id: int, target_id: int) -> None:
        super().__init__(__class__.__name__)
        self.properties.agent_id = agent_id
        self.properties.target_id = target_id
        self.agent: Agent = Object.objects_dict[agent_id]
        self.target: Agent = Object.objects_dict[target_id]

    def execute(self) -> str:
        print(self)
        return str(self)
