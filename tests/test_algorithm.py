from src.algorithm import find_conclusion


def test_find_conclusion_no_one_installed_game_means_red():
    assert find_conclusion(['not installed', 'not installed']) == 'RED'

# TODO: Add more tests for find_conclusion! At least enough to cover states RED, YELLOW and GREEN
