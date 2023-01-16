from typing import Dict, List

from src.actions.action import Action
from src.common.point import Point
from src.common.serializable import Properties
from src.objects.interactive_object import InteractiveObject
from src.objects.object import Object


class NearbyObjects(Action):
    """
    Action to retrieve nearby objects around the triggering object
    """
    base: str
    properties: Properties
    agent_position: Point
    objects_map: Dict[Point, List[Object]]
    range: int

    def __init__(self, agent: 'Agent', range: int = 1) -> None:
        super().__init__()
        self.objects_map = agent.scene.objects_map
        self.agent_position = agent.properties.position
        self.properties.agent_id = agent.properties.id
        self.range = range

    def execute(self) -> None:
        self.properties.nearby_objects = self.__get_nearby_objects()
        # should be changed to a log as list containing nearby items
        self.log()

    def __get_nearby_objects(self):
        objects = []
        for i in range(-self.range, self.range+1):
            for j in range(-self.range, self.range+1):
                object_map = self.objects_map.get(self.agent_position.__add__(Point(i, j)))
                if object_map is None:
                    continue

                objects.extend(list(
                    filter(lambda x: (issubclass(x.__class__, InteractiveObject)), object_map)))
        return list(map(lambda x: (
            {
                'class_name': x.__class__.__name__,
                'id': x.properties.id,
                'position': x.properties.position
            }
        ), objects))
