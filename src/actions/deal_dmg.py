from typing import Union

from src.actions.action import Action
from src.actions.die import Die
from src.common.serializable import Properties
from src.objects.npc import NPC


class DealDmg(Action):
    """
    Simple action for dealing damage.
    """
    base: str
    properties: Properties
    target: Union['Agent', NPC]

    def __init__(self, target: Union['Agent', NPC], dmg: int) -> None:
        super().__init__()
        self.properties.object_id = target.properties.id
        self.target = target
        self.properties.dmg = dmg

    def execute(self) -> None:
        self.target.hp -= self.properties.dmg
        self.log()
        if self.target.hp <= 0:
            Die(self.target).execute()
