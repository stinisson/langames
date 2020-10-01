from src.algorithm import conclusion
from pathlib import Path
import json


# def conclusion(states):
#     if 'not owned' in states:
#         return 'RED'
#     if 'not installed' in states:
#         return 'YELLOW'
#     return 'GREEN'

def test_find_conclusion_no_one_owned_game_means_red():
    assert conclusion(['not owned', 'not installed']) == 'RED'


def test_find_conclusion_no_one_installed_game_means_yellow():
    assert conclusion(['owned', 'not installed']) == 'YELLOW'


def test_find_conclusion_installed_game_means_green():
    assert conclusion(['owned', 'installed']) == 'GREEN'


# TODO: Add tests for find_gamers. Hint: either load data/gamers.json into the test, or make up some test data here!
# (do you prefer separate test data file, or hard-coding the test data in the test? Discuss!)

# def find_gamers(data):
#     return {gamer['name'] for gamer in data['gamers']}

def test_find_first_gamer():
    data = json.loads(Path('test_gamers.json').read_text(encoding='utf8'))
    gamer = data['gamers'][0]['name']
    assert gamer == "Agneta"


def test_find_all_gamers():
    data = json.loads(Path('test_gamers.json').read_text(encoding='utf8'))
    all_gamers = [gamer['name'] for gamer in data['gamers']]
    assert all_gamers == ['Agneta', 'Anni-Frid', 'Björn', 'Benny']
