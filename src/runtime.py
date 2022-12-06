from typing import List, Optional

from src.actions.next_scene import NextScene
from src.common.exec_interrupt import MapExit


class Runtime:
    """
    Supplies basic execution of users code across various levels.
    """
    agents_code: str
    interactive: bool
    next_scene: NextScene
    scene: Optional['Scene']
    scenes: List['Scene']

    def __init__(self, agents_code_path: str, interactive: bool) -> None:
        self.agents_code_path = agents_code_path
        self.scene = None
        self.scenes = []
        self.next_scene = NextScene(self)
        self.interactive = interactive

    def run(self) -> None:
        """
        Run scenes as longs as during scene's run
        a next scene is called. `MapExit` is
        raised when player finishes a scene and reaches
        a portal.
        """
        self.next_scene.execute()
        max_scenes: int = 8
        scenes: int = 0
        while scenes < max_scenes:
            try:
                scenes += 1
                self.scene.run()
            except MapExit:
                # Execution stopped
                pass
            except Exception:
                self.next_scene.execute()