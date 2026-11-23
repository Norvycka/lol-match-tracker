import os
import httpx
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
HEADERS = {"X-Riot-Token": API_KEY}  # made once, reused by every function


def get_puuid(game_name, tag_line):
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    response = httpx.get(url, headers=HEADERS)
    puuid = response.json()["puuid"]  # take the puuid out of the response
    return puuid


# print(get_puuid("KoKayn", "Vycka"))
# print(get_puuid("RaiderGO", "TWTV1"))


def get_match_ids(puuid, count=5):
    match_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count={count}"
    match_response = httpx.get(match_url, headers=HEADERS)
    return match_response.json()


def get_match(match_id):
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}"  # which input goes in the URL?
    response = httpx.get(url, headers=HEADERS)
    return response.json()  # the data, not the envelope


puuid = get_puuid("KoKayn", "Vycka")
ids = get_match_ids(puuid, 3)
print(ids)  # should be 3 IDs
match = get_match(ids[0])
print(match["info"]["gameDuration"])  # length of your last game, in seconds
