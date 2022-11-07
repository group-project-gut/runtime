from .action import Action
from .enums import Direction
from .agent import Agent


class Move(Action):
    def __init__(self, agent: Agent, direction: Direction) -> None:
        super().__init__(agent.properties.id, agent.properties.id)
        self.properties.direction: Direction = direction

    def execute(self) -> str:
        self.agent.properties.position += self.properties.direction.value
        return super().execute()
