from src.objects.object import Object
from src.objects.agent import Agent
from src.common.serializable import Serializable


class Action(Serializable):
    def __init__(self) -> None:
        super().__init__(__class__.__name__)

    def execute(self) -> str:
        print(self)
        return str(self)
