from typing import List

from src.common.point import Point
from src.common.serializable import Serializable


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
        self.name = self.__class__.__name__
        self.walkable = False

        scene.add_object_to_position_map(self, position)
        scene.add_object_to_id_map(self)
        scene.increment_last_object_id()

        # Log creation of the `Object`
        print(self)

    def occupied_fields(self, current_position: Point = None) -> List[Point]:
        if not current_position:
            current_position = self.properties.position
        return [current_position]

    def tick(self) -> None:
        """
        Called every turn of the object to perform actions
        """

    def on_collision(self, other) -> None:
        """
        This method is called when other `Object` enters
        the `field` this object is on.
        """
