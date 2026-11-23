from riot_api import get_puuid, get_match_ids, get_match, find_player
from stats import win_rate, current_streak

puuid = get_puuid("KoKayn", "Vycka")

games = []
for match_id in get_match_ids(puuid):
    match = get_match(match_id)
    games.append(find_player(match, puuid))  # what do you append? (use find_player)

print("win rate:", win_rate(games))
print("streak:", current_streak(games))
