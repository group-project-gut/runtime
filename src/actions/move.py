from src.common.enums import Direction
from src.common.point import Point
from .action import Action


class Move(Action):
    '''
    Simple action for changing position of `Agent`. It does not log anything
    in case the movement was not possible(destination is not walkable etc).
    '''

    def __init__(self, agent, direction: Direction) -> None:
        super().__init__()
        self.properties.agent_id = agent.properties.id
        self.agent = agent
        self.properties.direction: Direction = direction

    def execute(self, scene) -> str:
        new_position: Point = self.agent.properties.position + \
            self.properties.direction.value

        scene.move_object(self.agent, new_position)

        # Logging happens before collision detection
        # because it may result in loading next scene,
        # so we must ensure proper order of logs.
        self.log()

        scene.check_collisions(self.agent)
