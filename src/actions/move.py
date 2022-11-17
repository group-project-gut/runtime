from src.scene import Scene
from .action import Action
from src.common.enums import Direction
from src.common.point import Point
from src.objects.agent import Agent


class Move(Action):
    def __init__(self, agent: Agent, direction: Direction) -> None:
        super().__init__()
        self.properties.agent_id = agent.properties.id
        self.agent: Agent = agent
        self.properties.direction: Direction = direction

    def execute(self, scene: Scene) -> str:
        new_position: Point = self.agent.properties.position + self.properties.direction.value
        if scene[new_position] is not None and scene[new_position][0].walkable:
            scene[self.agent.properties.position].remove(self.agent)
            scene[new_position].append(self.agent)
            self.agent.properties.position = new_position

            ret = super().execute()

            for collision_object in scene[new_position]:
                collision_object.on_collision(self.agent)

            return ret
