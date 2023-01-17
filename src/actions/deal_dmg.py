from typing import Union
from src.actions.action import Action
from src.common.serializable import Properties


class DealDmg(Action):
    """
    Simple action for dealing damage.
    """
    base: str
    properties: Properties
    target: Union['Agent', 'NPC']

    def __init__(self, target: Union['Agent', 'NPC'], dmg: int) -> None:
        super().__init__()
        self.properties.object_id = target.properties.id
        self.target = target
        self.dmg = dmg
        self.properties.dmg = dmg

    def execute(self) -> None:
        self.target.hp -= self.dmg
        self.log()
