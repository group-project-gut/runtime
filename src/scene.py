from src.actions.create_scene import CreateScene
from src.common.point import Point
from src.objects.agent import Agent
from src.objects.floor import Floor
from src.objects.portal import Portal
from .objects.object import Object


class Scene():
    def __init__(self) -> None:
        self.objects_count = 0
        self.objects_map = {}
        self.objects_dict = {}
        self.__player: Agent = Agent(self)
        self.__create: CreateScene = CreateScene()
        
        Portal(self, Point(0,1))
        for x in range(5):
            for y in range(5):
                Floor(self, Point(x, y))

    def __getitem__(self, indices) -> Object:
        return self.objects_map.get(indices)

    def get_player(self):
        return self.__player

    def add_object_to_map(self, new_object: Object) -> None:
        if self.objects_map.get(new_object.properties.position) is None:
            self.objects_map[new_object.properties.position] = [new_object]
        else:
            self.objects_map[new_object.properties.position].append(new_object)
        print(new_object)

    def create(self) -> None:
        self.__create.execute(self)