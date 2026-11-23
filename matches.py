from stats import win_rate
from stats import win_rate, current_streak

matches = [
    {"champion": "Rengar", "kills": 12, "deaths": 3, "win": True},
    {"champion": "Talon", "kills": 4, "deaths": 9, "win": False},
    {"champion": "Rengar", "kills": 8, "deaths": 5, "win": True},
    {"champion": "Ahri", "kills": 6, "deaths": 6, "win": False},
    {"champion": "Rengar", "kills": 3, "deaths": 7, "win": False},
]


print(win_rate(matches), "expected 40.0")


test1 = [{"win": False}, {"win": False}, {"win": False}, {"win": True}, {"win": False}]
test2 = [{"win": True}, {"win": False}, {"win": True}, {"win": True}, {"win": True}]
test3 = [{"win": True}, {"win": True}, {"win": True}, {"win": True}, {"win": True}]

print(current_streak(test1), "expected 3L")
print(current_streak(test2), "expected 1W")
print(current_streak(test3), "expected 5W")
