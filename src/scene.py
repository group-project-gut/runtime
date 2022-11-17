from src.actions.create_scene import CreateScene
from src.common.point import Point
from src.objects.agent import Agent
from src.objects.floor import Floor
from src.objects.portal import Portal
from .objects.object import Object


class Scene():
    '''
    Object representing one level in the game.
    It is responsible for storing all instances of `Object` class.
    '''
    def __init__(self) -> None:
        self.objects_count = 0
        self.objects_map = {}
        self.objects_dict = {}
        self.create: CreateScene = CreateScene()

        # The abstraction is not the best here
        # but I think it's much better than creating
        # constructor taking an bool `log` or sth.
        # It is necessary, because `Scene` constructor
        # is called by `create_scene` action, so we
        # always get a fresh scene whenever we want.
        # How it works? If there isn't a variable `Player`
        # it means that it's te first time `Scene` was
        # constructed, so it has to be done manualy -
        # - not through `scene.create.execute()`
        if not hasattr(self,'_Scene__player'):
            self.create.log()

        self.__player: Agent = Agent(self)

        # It's an example init sequence
        # called each time the player goes through a portal
        Portal(self, Point(0, 1))
        for x in range(5):
            for y in range(5):
                Floor(self, Point(x, y))

    def __getitem__(self, indices) -> Object:
        return self.objects_map.get(indices)

    def get_player(self):
        '''
        Returns reference to a players agent.
        We cannot use just the field `__player`
        because the reference itself my change
        during runtime and could become outdated.
        Think of actions like `move` which need
        agent that is in the game now, not a
        reference to agent in a previous scene
        '''
        return self.__player

    def add_object_to_map(self, new_object: Object) -> None:
        '''
        Add object to per scene storage indexed by objects position.
        The storage can store multiple objects and for now, object at
        index `0` is a `field`(`floor`).
        '''
        if self.objects_map.get(new_object.properties.position) is None:
            self.objects_map[new_object.properties.position] = [new_object]
        else:
            self.objects_map[new_object.properties.position].append(new_object)
