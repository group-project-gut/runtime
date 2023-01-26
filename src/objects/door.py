from typing import List

from src.common.point import Point
from src.objects.interactive_object import InteractiveObject
from src.objects.key import Key


class Door(InteractiveObject):
    """
    `Object` interacting with a key
    """
    __keys: List[int]  # collection of key's ids which can open the door

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(position, scene)
        self.properties.is_open = False
        self.__keys = []

    def try_open(self, triggering_object) -> None:
        if self.can_open(triggering_object.get_equipment()):
            self.properties.is_open = True
            print(self)

    def add_key(self, key: Key):
        self.__keys.append(key.properties.id)

    def can_open(self, items: list):
        return any(item in self.__keys for item in items)
