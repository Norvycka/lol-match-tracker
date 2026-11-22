from stats import win_rate

matches = [
    {"champion": "Rengar", "kills": 12, "deaths": 3, "win": True},
    {"champion": "Talon", "kills": 4, "deaths": 9, "win": False},
    {"champion": "Rengar", "kills": 8, "deaths": 5, "win": True},
    {"champion": "Ahri", "kills": 6, "deaths": 6, "win": False},
    {"champion": "Rengar", "kills": 3, "deaths": 7, "win": False},
]


print(win_rate(matches))
