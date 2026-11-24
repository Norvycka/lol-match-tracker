def win_rate(games: list[dict]) -> float | None:
    if len(games) == 0:
        return None

    total = len(games)
    wins = 0
    for game in games:
        if game["win"] == True:
            wins = wins + 1
    return wins / total * 100


def current_streak(games: list[dict]) -> str | None:
    if len(games) == 0:
        return None

    first_result = games[0][
        "win"
    ]  # was the NEWEST game a win or a loss? (True / False)
    count = 0
    for game in games:
        if game["win"] == first_result:  # same result as the newest game?
            count = count + 1
        else:
            break  # streak broken, stop counting
    if first_result == True:
        return f"{count}W"
    else:
        return f"{count}L"
