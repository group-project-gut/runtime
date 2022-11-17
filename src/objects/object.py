from src.common.point import Point
from src.common.serializable import Serializable


class Object(Serializable):

    def __init__(self, position: Point, scene) -> None:
        super().__init__(__class__.__name__)
        self.properties.id: int = scene.objects_count
        self.properties.position: Point = position
        self.scene = scene
        self.walkable = False

        scene.add_object_to_map(self)
        scene.objects_dict[self.properties.id] = self
        scene.objects_count += 1

    def on_collision(self, other) -> None:
        pass
