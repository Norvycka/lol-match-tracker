import asyncio
import time
import httpx
from riot_api import get_puuid, get_match_ids, get_match, find_player
from stats import win_rate, current_streak


async def main():
    start = time.perf_counter()

    async with httpx.AsyncClient() as client:  # ONE client, shared by every request
        puuid = await get_puuid(
            client, "KoKayn", "Vycka"
        )  # await get_puuid with client + your Riot ID
        ids = await get_match_ids(client, puuid)  # await get_match_ids
        matches = await asyncio.gather(
            *[get_match(client, mid) for mid in ids]
        )  # all matches at once

    games = []
    for match in matches:  # no Riot calls here, just looking through data
        result = find_player(match, puuid)
        if result is not None:
            games.append(result)

    print("win rate:", win_rate(games))
    print("streak:", current_streak(games))
    print(f"took {time.perf_counter() - start:.2f} seconds")


asyncio.run(main())
