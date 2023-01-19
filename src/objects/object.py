from src.common.point import Point
from src.common.serializable import Serializable, Properties


class Object(Serializable):
    """
    Abstract object existing in a `scene`. Represents part of scene's state,
    in contrast to `Action` which represents only modifications of the state.
    """
    scene: 'Scene'
    walkable: bool

    def __init__(self, position: Point, scene: 'Scene') -> None:
        super().__init__(__class__.__name__)
        self.properties.id = scene.last_object_id  # int
        self.properties.position = position  # Point
        self.scene = scene
        self.walkable = False

        scene.add_object_to_position_map(self, position)
        scene.add_object_to_id_map(self)
        scene.increment_last_object_id()

        # Log creation of the `Object`
        print(self)

    def occupy_field(self, position: Point) -> bool:
        self.scene.get_objects_by_position(position).append(self)
        return True

    def free_field(self, position: Point) -> None:
        self.scene.get_objects_by_position(position).remove(self)
        return True

    def tick(self) -> None:
        """
        Called every turn of the object to perform actions
        """

    def on_collision(self, other) -> None:
        """
        This method is called when other `Object` enters
        the `field` this object is on.
        """
