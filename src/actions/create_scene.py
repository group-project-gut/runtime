from src.objects.portal import Portal
from src.objects.floor import Floor
from .action import Action
from src.common.point import Point


class CreateScene(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, scene) -> str:
        ret = super().execute()

        scene.__init__()
        
        return ret
