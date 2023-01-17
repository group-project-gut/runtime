import random
from typing import Dict, List

from src.common.point import Point
from src.objects.agent import Agent
from src.objects.floor import Floor
from src.objects.portal import Portal
from src.objects.object import Object
from src.objects.npcs.enemies.training_dummy import TrainingDummy


class Scene:
    """
    Object representing one level in the game.
    It is responsible for storing all instances of `Object` class.
    """
    objects_count: int
    objects_map: Dict[Point, List[Object]]  # fields
    objects_dict: Dict[int, Object]
    agent_locals: Dict
    runtime: 'Runtime'
    __player: Agent

    def __init__(self, runtime) -> None:
        self.objects_count = 0
        self.objects_map = {}
        self.objects_dict = {}
        self.agent_locals = {}
        self.runtime = runtime
        self.__player = Agent(self)

        self._generate_scene()

    def _generate_scene(self):
        """
        For now it'll generate scene layout
        Subject to be changed
        """
        STEPS = 20
        pos = Point(0, 0)
        points = [pos]
        for _ in range(STEPS):
            pos += Point(random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))
            points.append(pos)
            points.append(pos + Point(-1, 0))
            points.append(pos + Point(1, 0))
            points.append(pos + Point(0, -1))
            points.append(pos + Point(0, 1))

        points = list(dict.fromkeys(points))  # remove duplicates

        for point in points:
            Floor(self, point)

        Portal(self, random.choice(points))
        TrainingDummy(self, Point(1, 0))

    def __getitem__(self, indices) -> Object:
        return self.objects_map.get(indices)

    def run(self):
        """
        TODO
        """
        max_spins: int = 8
        spins: int = 0
        while spins < max_spins:
            spins += 1
            for scene_object in list(self.objects_dict.values()):
                scene_object.tick()

    def get_player(self):
        """
        Returns reference to a players agent.
        We cannot use just the field `__player`
        because the reference itself my change
        during runtime and could become outdated.
        Think of actions like `move` which need
        agent that is in the game now, not a
        reference to agent in a previous scene
        """
        return self.__player

    def move_object(self, moved_object: Object, new_position: Point) -> bool:
        """
        Returns True on successful `move` operation
        """

        # Check if the destination is a `field` in the scene, and if it is -
        # - it must be walkable
        if not self.is_walkable_field(new_position):
            return False

        self[moved_object.properties.position].remove(moved_object)
        self[new_position].append(moved_object)
        moved_object.properties.position = new_position
        return True

    def is_walkable_field(self, position: Point):
        return self[position] and self[position][0].walkable

    def check_collisions(self, entering_object: Object) -> None:
        """
        Call `on_collision` callback of every Object in the same
        field as `entering_object`.
        """
        for collision_object in self[entering_object.properties.position]:
            if collision_object != entering_object:
                collision_object.on_collision(entering_object)

    def add_object_to_map(self, new_object: Object) -> None:
        """
        Add object to per scene storage indexed by objects position.
        The storage can store multiple objects and for now, object at
        index `0` is a `field`(`floor`).
        """
        if self.objects_map.get(new_object.properties.position) is None:
            self.objects_map[new_object.properties.position] = [new_object]
        else:
            self.objects_map[new_object.properties.position].append(new_object)
