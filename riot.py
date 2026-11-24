from riot_api import get_puuid, get_match_ids, get_match, find_player
from stats import win_rate, current_streak
import time

puuid = get_puuid("KoKayn", "Vycka")

start = time.perf_counter()

games = []
for match_id in get_match_ids(puuid):
    match = get_match(match_id)
    result = find_player(match, puuid)
    if find_player is not None:
        games.append(result)

print("win rate:", win_rate(games))
print("streak:", current_streak(games))

print(f"took {time.perf_counter() - start:.2f} seconds")
