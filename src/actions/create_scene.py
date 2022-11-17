from src.objects.floor import Floor
from src.runtime import Runtime
from src.scene import Scene
from .action import Action
from src.common.point import Point


class CreateScene(Action):
    def __init__(self) -> None:
        super().__init__(-1, -1)

    def execute(self) -> str:
        for x in range(5):
            for y in range(5):
                Runtime.scene.add_object(Floor(Point(x, y)))
