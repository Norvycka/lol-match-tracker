import os
import httpx
from dotenv import load_dotenv
import asyncio

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
HEADERS = {"X-Riot-Token": API_KEY}  # made once, reused by every function
SEM = asyncio.Semaphore(5)


async def riot_get(client: httpx.AsyncClient, url: str) -> dict | list:
    async with SEM:
        while True:
            response = await client.get(url, headers=HEADERS)
            if response.status_code == 200:
                return response.json()
            if response.status_code == 429:
                wait = int(response.headers["Retry-After"])
                print(f"429! waiting {wait}s before retrying {url}")
                await asyncio.sleep(wait)  # wait, the async way

            else:
                response.raise_for_status()  # any other error: stop with a clear message


async def get_puuid(client: httpx.AsyncClient, game_name: str, tag_line: str) -> str:
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    data = await riot_get(client, url)
    return data["puuid"]


async def get_match_ids(
    client: httpx.AsyncClient, puuid: str, count: int = 5
) -> list[str]:
    match_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count={count}"
    return await riot_get(client, match_url)


async def get_match(client: httpx.AsyncClient, match_id: str) -> dict:
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}"  # which input goes in the URL?
    return await riot_get(client, url)


def find_player(match: dict, puuid: str) -> dict | None:
    for player in match["info"]["participants"]:
        if player["puuid"] == puuid:
            return {
                "champion": player["championName"],
                "kills": player["kills"],
                "deaths": player["deaths"],
                "win": player["win"],
            }
