import random
from typing import Dict, List

from src.common.point import Point
from src.objects.agent import Agent
from src.objects.floor import Floor
from src.objects.portal import Portal
from src.objects.object import Object
from src.objects.npcs.enemies.training_dummy import TrainingDummy
from src.objects.npcs.enemies.bear import Bear


class Scene:
    """
    Object representing one level in the game.
    It is responsible for storing all instances of `Object` class.
    """
    agent_locals: Dict
    last_object_id: int
    runtime: 'Runtime'
    _objects_position_map: Dict[Point, List[Object]]  # fields
    _objects_id_map: Dict[int, Object]
    __player: Agent

    def __init__(self, runtime) -> None:
        self.last_object_id = 0
        self._objects_position_map = {}
        self._objects_id_map = {}
        self.agent_locals = {}
        self.runtime = runtime

        self._generate_scene_small()

        self.__player = Agent(self)

    def _generate_scene_small(self) -> None:
        """
        Small scene for tests
        """
        points = [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1), Point(0, 2), Point(1, 2)]

        for point in points:
            Floor(self, point)

        # Portal(self, random.choice(points))
        Bear(self, Point(0, 1))

    def _generate_scene(self) -> None:
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

    def run(self) -> None:
        """
        TODO
        """
        max_spins: int = 8
        spins: int = 0
        while spins < max_spins:
            spins += 1
            for scene_object in list(self._objects_id_map.values()):
                scene_object.tick()

    def get_player(self) -> Agent:
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

    def get_objects_by_position(self, position) -> List[Object]:
        return self._objects_position_map[position]

    def get_object_by_id(self, id) -> Object:
        return self._objects_id_map[id]

    def remove_object_from_occupied_fields(self, object: Object):
        for field in object.occupied_fields():
            self._objects_position_map.get(field).remove(object)

    def occupy_fields(self, object: Object, fields: Point = None):
        if not fields:
            fields = object.occupied_fields()
        for field in fields:
            self._objects_position_map.get(field).append(object)

    def move_object(self, moved_object: Object, new_position: Point) -> bool:
        """
        Returns True on successful `move` operation
        """

        # Check if all fields requested are `walkable`
        for field in moved_object.occupied_fields(new_position):
            if not self.is_walkable_field(field):
                return False

        # Now we can free previous fields
        self.remove_object_from_occupied_fields(moved_object)

        # ... and occupy new ones!
        moved_object.properties.position = new_position
        self.occupy_fields(moved_object)

        return True

    def is_walkable_field(self, position: Point) -> bool:
        return self._objects_position_map.get(position) and self._objects_position_map[position][0].walkable

    def check_collisions(self, entering_object: Object) -> None:
        """
        Call `on_collision` callback of every Object in the same
        field as `entering_object`.
        """
        for collision_object in self._objects_position_map[entering_object.properties.position]:
            if collision_object != entering_object:
                collision_object.on_collision(entering_object)

    def increment_last_object_id(self) -> None:
        self.last_object_id += 1

    def add_object_to_position_map(self, new_object: Object, position: Point) -> None:
        """
        Add object to per scene storage indexed by objects position.
        The storage can store multiple objects and for now, object at
        index `0` is a `field`(`floor`).
        """
        if self._objects_position_map.get(position) is None:
            self._objects_position_map[position] = []

        for field in new_object.occupied_fields():
            self._objects_position_map.get(field).append(new_object)

    def add_object_to_id_map(self, new_object: Object) -> None:
        """
        Add object to per scene storage indexed by objects `id`.
        """
        self._objects_id_map[new_object.properties.id] = new_object

    def remove_object_from_id_map(self, object: Object) -> None:
        del self._objects_id_map[object.properties.id]
