from src.common.point import Point
from src.common.serializable import Serializable


class Object(Serializable):
    '''
    Abstract object existing in a `scene`. Represents part of scene's state,
    in contrast to `Action` which represents only modifications of the state.
    '''

    def __init__(self, position: Point, scene) -> None:
        super().__init__(__class__.__name__)
        self.properties.id: int = scene.objects_count
        self.properties.position: Point = position
        self.scene = scene
        self.walkable = False

        scene.add_object_to_map(self)
        scene.objects_dict[self.properties.id] = self
        scene.objects_count += 1

        # Log creation of the `Object`
        print(self)

    def tick(self) -> None:
        '''
        Called every turn of the object to perform actions
        '''

    def on_collision(self, other) -> None:
        '''
        This method is called when other `Object` enters
        the `field` this object is on.
        '''
