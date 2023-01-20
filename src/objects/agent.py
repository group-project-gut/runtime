from src.actions.use import Use
from src.actions.move import Move
from src.actions.nearby_objects import NearbyObjects
# from src.actions.pick_up import PickUp
from src.actions.wave import Wave
from src.actions.attacks.slash import Slash
from src.common.enums import Direction
from src.common.point import Point
from src.objects.object import Object
from src.actions.wait_for_code import WaitForCode

AGENT_HP = 100


class Agent(Object):
    """
    Simple agent existing in a `scene`.
    """
    items: list
    hp: int

    def __init__(self, scene: 'Scene', position: Point = Point(0, 0)) -> None:
        super().__init__(position, scene)
        self.items = []
        self.wait_for_code: WaitForCode = WaitForCode(self.scene.runtime.interactive)
        self.hp = AGENT_HP

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
            'slash': lambda direction: Slash(self, direction).execute(),
            'wave': Wave(self).execute,
            'Direction': Direction,
            'len': len,
            'range': range,
            'enumerate': enumerate,
            'nearby_objects': NearbyObjects(self).execute,
            'interact': lambda object_id, action: Use(self, object_id, action).execute()
        }

        # Sure, I know exec bad
        # pylint: disable=exec-used
        exec(
            code,
            # It violates lasagna code rule but I guess its ok
            {'__builtins__': agent_builtins},
            self.scene.agent_locals,
        )
