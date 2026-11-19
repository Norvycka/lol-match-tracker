matches = [
    {"champion": "Rengar", "kills": 12, "deaths": 3, "win": True},
    {"champion": "Talon", "kills": 4, "deaths": 9, "win": False},
    {"champion": "Rengar", "kills": 8, "deaths": 5, "win": True},
    {"champion": "Ahri", "kills": 6, "deaths": 6, "win": False},
    {"champion": "Rengar", "kills": 3, "deaths": 7, "win": False},
]


def win_rate(games):
    total = len(games)
    wins = 0
    for game in games:
        if game["win"] == True:
            wins = wins + 1
    return wins / total * 100


print(win_rate(matches))
