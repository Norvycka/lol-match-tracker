def win_rate(games):
    total = len(games)
    wins = 0
    for game in games:
        if game["win"] == True:
            wins = wins + 1
    return wins / total * 100
