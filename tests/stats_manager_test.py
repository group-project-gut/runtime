from src.objects.agent.stats_manager import StatsManager, LEVEL_TRESHOLDS


def test_set_level():
    sm = StatsManager()
    sm.level = 3
    assert sm.experience == LEVEL_TRESHOLDS[1]


def test_get_level():
    sm = StatsManager()
    sm.experience = LEVEL_TRESHOLDS[2] + 1
    assert sm.level == 4
