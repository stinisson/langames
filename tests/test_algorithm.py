from src.algorithm import conclusion, find_gamers
from pathlib import Path
import json
import os


# test conclusion()
def test_conclusion_not_owned_means_red():
    assert conclusion(['not owned', 'not installed', 'installed', 'not installed']) == 'RED'


def test_conclusion_not_owned_means_red_last():
    assert conclusion(['not installed', 'not installed', 'installed', 'not owned']) == 'RED'


def test_conclusion_empty_list_means_not_red():
    assert conclusion(['']) != 'RED'


def test_conclusion_not_installed_means_yellow():
    assert conclusion(['owned', 'not installed']) == 'YELLOW'


def test_conclusion_multiple_not_installed_means_yellow():
    assert conclusion(['owned', 'not installed', 'not installed', 'owned', 'owned']) == 'YELLOW'


def test_conclusion_empty_list_means_not_yellow():
    assert conclusion(['']) != 'YELLOW'


def test_conclusion_installed_means_green():
    assert conclusion(['installed', 'installed']) == 'GREEN'


def test_conclusion_empty_list_means_green():
    assert conclusion(['']) == 'GREEN'


# test find_gamers()
def test_find_gamers_first_gamer_hard_coded_data():
    data = {
        "gamers": [
            {
                "name": "Agneta",
                "games": [
                    {
                        "game": "Alien Swarm",
                        "installed": True
                    },
                    {
                        "game": "Quake III: Arena",
                        "installed": True
                    },
                    {
                        "game": "Wreckfest",
                        "installed": False
                    },
                    {
                        "game": "Brawlhalla",
                        "installed": True
                    }
                ]
            }
        ]
    }
    gamers = find_gamers(data)
    assert "Agneta" in gamers


def test_find_gamers_find_gamer_in_data_loaded_into_test_from_file():
    data = json.loads(Path('../data/gamers.json').read_text(encoding='utf8'))
    all_gamers = find_gamers(data)
    assert "Agneta" in all_gamers


def test_find_gamers_gamer_not_in_data_loaded_into_test_from_file():
    data = json.loads(Path('../data/gamers.json').read_text(encoding='utf8'))
    all_gamers = find_gamers(data)
    assert "ABBA" not in all_gamers


# If gamers never change, otherwise bananas
def test_find_gamers_find_all_gamers():
    data = json.loads(Path('../data/gamers.json').read_text(encoding='utf8'))
    all_gamers = find_gamers(data)
    assert all_gamers == {'Agneta', 'Anni-Frid', 'Björn', 'Benny'}


# from lesson
def test_find_gamers():
    print(os.getcwd())
    expected = []
    obj = Path("../data/gamers.json").read_text(encoding="utf8")

    actual = find_gamers(obj)
    assert actual == expected
