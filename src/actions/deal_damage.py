from typing import Union
from src.actions.action import Action
from src.common.serializable import Properties


class DealDamage(Action):
    """
    Simple action for dealing damage.
    """
    base: str
    properties: Properties
    target: Union['Agent', 'NPC']

    def __init__(self, target: Union['Agent', 'NPC'], damage: int) -> None:
        super().__init__()
        self.properties.object_id = target.properties.id
        self.target = target
        self.damage = damage

    def execute(self) -> None:
        self.target.hp -= self.damage
        self.log()
