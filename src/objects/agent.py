from src.actions.move import Move
from src.actions.wave import Wave
from src.common.enums import Direction
from src.common.point import Point
from src.objects.object import Object
from src.common.serializable import Properties
from src.actions.wait_for_code import WaitForCode


class Agent(Object):
    """
    Simple agent existing in a `scene`.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool
    hp: int

    def __init__(self, scene: 'Scene', hp: int, position: Point = Point(0, 0)) -> None:
        super().__init__(position, scene)
        self.wait_for_code: WaitForCode = WaitForCode(self.scene.runtime.interactive)
        self.hp = hp

    def tick(self) -> None:
        """
        Called on an `Object`, so it can perform some actions
        """
        self.wait_for_code.execute()

        # Users code was uploaded, so we can safely read the file
        with open(self.scene.runtime.agents_code_path, 'r', encoding="UTF-8") as code_file:
            code: str = code_file.read()

        agent_builtins = {
            'move': lambda direction: Move(self, direction).execute(),
            'wave': Wave(self).execute,
            'Direction': Direction,
            'len': len,
            'range': range,
            'enumerate': enumerate,
        }

        # Sure, I know exec bad
        # pylint: disable=exec-used
        exec(
            code,
            # It violates lasagna code rule but I guess its ok
            {'__builtins__': agent_builtins},
            self.scene.agent_locals,
        )
