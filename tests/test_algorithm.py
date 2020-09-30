from src.algorithm import conclusion


def test_find_conclusion_no_one_installed_game_means_red():
    assert conclusion(['not installed', 'not installed']) == 'RED'

# TODO: Add more tests for find_conclusion! At least enough to cover states RED, YELLOW and GREEN


# TODO: Add tests for find_gamers. Hint: either load data/gamers.json into the test, or make up some test data here!
# (do you prefer separate test data file, or hard-coding the test data in the test? Discuss!)


