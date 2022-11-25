from src.actions.move import Move
from src.common.enums import Direction
from src.common.point import Point
from .object import Object


class Agent(Object):
    '''
    Simple agent existing in a `scene`.
    '''

    def __init__(self, scene, position: Point = Point(0, 0)):
        super().__init__(position, scene)

    def tick(self) -> None:
        '''
        Called on an `Object`, so it can perform some actions
        '''
        agent_builtins = {
            'move': lambda direction: Move(
                self,
                direction).execute(
                self.scene),
            'Direction': Direction,
            'len': len,
            'range': range,
            'enumerate': enumerate,
        }

        # Sure, I know exec bad
        # pylint: disable=exec-used
        exec(
            self.scene.runtime.agents_code,
            # It violates lasagna code rule but I guess its ok
            {'__builtins__': agent_builtins},
            self.scene.agent_locals,
        )
