import os
import httpx
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
HEADERS = {"X-Riot-Token": API_KEY}  # made once, reused by every function


def riot_get(url: str):
    response = httpx.get(url, headers=HEADERS)
    response.raise_for_status()  # any bad status → clear error HERE, not 3 steps later
    return response.json()


def get_puuid(game_name: str, tag_line: str) -> str:
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    data = riot_get(url)
    puuid = data["puuid"]
    return puuid


def get_match_ids(puuid: str, count: int = 5) -> list[str]:
    match_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count={count}"
    return riot_get(match_url)


def get_match(match_id: str) -> dict:
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}"  # which input goes in the URL?
    return riot_get(url)


def find_player(match: dict, puuid: str) -> dict | None:
    for player in match["info"]["participants"]:
        if player["puuid"] == puuid:
            return {
                "champion": player["championName"],
                "kills": player["kills"],
                "deaths": player["deaths"],
                "win": player["win"],
            }


if __name__ == "__main__":
    puuid = get_puuid("KoKayn", "Vycka")
    ids = get_match_ids(puuid, 3)
    print(ids)  # should be 3 IDs
    match = get_match(ids[0])
    print(match["info"]["gameDuration"])  # length of your last game, in seconds
    print(find_player(get_match(ids[0]), get_puuid("KoKayn", "Vycka")))
