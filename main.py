from fastapi import FastAPI
import httpx, asyncio
from riot_api import get_puuid, get_match_ids, get_match, find_player
from stats import win_rate, current_streak

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/players/{game_name}/{tag_line}")
async def player(game_name: str, tag_line: str):
    async with httpx.AsyncClient() as client:
        puuid = await get_puuid(client, game_name, tag_line)
        ids = await get_match_ids(client, puuid)
        matches = await asyncio.gather(*[get_match(client, mid) for mid in ids])

    games = []
    for match in matches:
        result = find_player(match, puuid)
        if result is not None:
            games.append(result)

    return {"win_rate": win_rate(games), "current_streak": current_streak(games)}
