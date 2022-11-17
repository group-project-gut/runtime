from src.objects.portal import Portal
from src.objects.floor import Floor
from .action import Action
from src.common.point import Point


class CreateScene(Action):
    '''
    `Action` used to create next scene. Called on collision by `Portal`.
    '''

    def execute(self, scene) -> str:
        '''
        The execution of this `Action` is quite problematic, because
        it uses EXISTING instance of scene and calls it's constructor
        once again. Subject to futher refactoring.
        '''
        self.log()
        scene.__init__()
