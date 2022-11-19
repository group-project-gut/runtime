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

        # Check if the destination is a `field` in the scene, and if it is -
        # - it must be walkable
        if scene[new_position] is not None and scene[new_position][0].walkable:
            scene[self.agent.properties.position].remove(self.agent)
            scene[new_position].append(self.agent)
            self.agent.properties.position = new_position

            # Logging happens before collision detection
            # because it may result in loading next scene,
            # so we must ensure proper order of logs.
            self.log()

            for collision_object in scene[new_position]:
                collision_object.on_collision(self.agent)
