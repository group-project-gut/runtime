from src.common.point import Point
from src.common.serializable import Serializable


class Object(Serializable):
    __objects_count: int = 0
    objects_dict = {}  # An empty object

    def __init__(self, position: Point, scene) -> None:
        super().__init__(__class__.__name__)
        self.properties.id: int = Object.__objects_count
        self.properties.position: Point = position
        self.scene = scene
        self.walkable = False

        Object.objects_dict[self.properties.id] = self
        Object.__objects_count += 1
