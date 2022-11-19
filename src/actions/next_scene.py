from src.scene import Scene
from .action import Action


class NextScene(Action):
    '''
    `Action` used to create next scene. Called on collision by `Portal`.
    '''

    def __init__(self, runtime) -> None:
        super().__init__()
        self.runtime = runtime

    def execute(self) -> None:
        '''
        The execution of this `Action` is quite problematic, because
        it uses EXISTING instance of scene and calls it's constructor
        once again. Subject to futher refactoring.
        '''
        self.log()
        self.runtime.scene = Scene(self.runtime)
        self.runtime.scenes.append(self.runtime.scene)
