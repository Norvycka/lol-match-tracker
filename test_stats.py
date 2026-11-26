from stats import win_rate, current_streak, average_kills
import pytest

MATCHES = [
    {"champion": "Rengar", "kills": 12, "deaths": 3, "win": True},
    {"champion": "Talon", "kills": 4, "deaths": 9, "win": False},
    {"champion": "Rengar", "kills": 8, "deaths": 5, "win": True},
    {"champion": "Ahri", "kills": 6, "deaths": 6, "win": False},
    {"champion": "Rengar", "kills": 3, "deaths": 7, "win": False},
]


def test_win_rate():
    assert win_rate(MATCHES) == 40.0


def test_win_rate_empty():
    assert win_rate([]) is None


def test_streak_empty():
    assert current_streak([]) is None


def test_streak_three_losses():
    games = [
        {"win": False},
        {"win": False},
        {"win": False},
        {"win": True},
        {"win": False},
    ]
    assert current_streak(games) == "3L"


def test_streak_one_win():
    games = [{"win": True}, {"win": False}, {"win": True}, {"win": True}, {"win": True}]
    assert current_streak(games) == "1W"


def test_streak_five_wins():
    games = [{"win": True}, {"win": True}, {"win": True}, {"win": True}, {"win": True}]
    assert current_streak(games) == "5W"


def test_average_kills():
    assert average_kills(MATCHES) == pytest.approx(6.6)
