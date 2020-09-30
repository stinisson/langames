def analyze(data, table_builder):
    games = sorted(find_games(data))
    gamers = sorted(find_gamers(data))
    table_builder.set_headers(["Game below, gamer ->"] + gamers + ["Conclusion"])
    for game in games:
        cells = [game]
        states = []
        for gamer in gamers:
            state = find_game_state(game=game, gamer=gamer, data=data)
            states.append(state)
            cells.append(state)
        cells.append(conclusion(states))
        table_builder.add_row(cells)


def find_games(data):
    games = set()
    for gamer in data['gamers']:
        for game in gamer['games']:
            games.add(game['game'])
    return games


def find_gamers(data):
    return {gamer['name'] for gamer in data['gamers']}


def find_game_state(game, gamer, data):
    for gamer_obj in data['gamers']:
        if gamer_obj['name'] == gamer:
            for game_obj in gamer_obj['games']:
                if game == game_obj['game']:
                    return 'installed' if game_obj['installed'] else 'not installed'
    return 'not owned'


def conclusion(states):
    if 'not owned' in states:
        return 'RED'
    if 'not installed' in states:
        return 'YELLOW'
    return 'GREEN'
