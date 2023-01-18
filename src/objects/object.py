from src.common.point import Point
from src.common.serializable import Serializable, Properties


class Object(Serializable):
    """
    Abstract object existing in a `scene`. Represents part of scene's state,
    in contrast to `Action` which represents only modifications of the state.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool

    def __init__(self, position: Point, scene: 'Scene') -> None:
        super().__init__(__class__.__name__)
        self.properties.id = scene.objects_count  # int
        self.properties.position = position  # Point
        self.scene = scene
        self.walkable = False

        scene.add_object_to_map(self, position)
        scene.objects_dict[self.properties.id] = self
        scene.objects_count += 1

        # Log creation of the `Object`
        print(self)

    def tick(self) -> None:
        """
        Called every turn of the object to perform actions
        """

    def on_collision(self, other) -> None:
        """
        This method is called when other `Object` enters
        the `field` this object is on.
        """
