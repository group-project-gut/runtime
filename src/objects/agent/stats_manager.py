AGENT_HP = 100
LEVEL_TRESHOLDS = [100, 300, 500, 1000, 1500, 2500]


class StatsManager:
    def __init__(self, experience=0, hp=AGENT_HP) -> None:
        self.experience = experience
        self.hp = hp

    @property
    def level(self) -> int:
        for i, treshold in enumerate(LEVEL_TRESHOLDS):
            if self.experience < treshold:
                return i + 1
        return len(LEVEL_TRESHOLDS) + 1

    @level.setter
    def level(self, new_val):
        if new_val == 1:
            self.experience = 0
            return

        for i, _ in enumerate(LEVEL_TRESHOLDS):
            if i + 1 == new_val:
                self.experience = LEVEL_TRESHOLDS[i - 1]
                return
        self.experience = LEVEL_TRESHOLDS[-1]
