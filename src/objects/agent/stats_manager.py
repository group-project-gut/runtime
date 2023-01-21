AGENT_HP = 100


class StatsManager:
    def __init__(self, experience=0, hp=AGENT_HP) -> None:
        self.experience = experience
        self.hp = hp

    def get_level(self) -> int:
        LEVEL_TRESHOLDS = [100, 300, 500, 1000, 1500, 2500]
        for i, treshold in enumerate(LEVEL_TRESHOLDS):
            if self.experience < treshold:
                return i + 1
        return len(LEVEL_TRESHOLDS) + 1
