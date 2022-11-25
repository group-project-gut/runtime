from src.actions.next_scene import NextScene
from src.common.exec_interrupt import MapExit
from src.scene import Scene


class Runtime:
    '''
    Supplies basic execution of users code across various levels.
    '''

    def __init__(self, agents_code: str) -> None:
        self.agents_code: str = agents_code
        self.scene: Scene = None
        self.scenes = []
        self.next_scene = NextScene(self)

    def run(self):
        '''
        Run scenes as longs as during scene's run
        a next scene is called. `MapExit` is
        raised when player finishes a scene and reaches
        a portal.
        '''
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
