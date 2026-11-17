import os
import httpx
from dotenv import load_dotenv

load_dotenv()  # read .env into the environment
API_KEY = os.getenv("RIOT_API_KEY")
print("key loaded:", API_KEY[:8] + "...")  # only print the start, never the whole key

GAME_NAME = os.getenv("GAME_NAME")  # your Riot ID: the part before the #
TAG_LINE = os.getenv("TAG_LINE")  # the part after the #

url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{GAME_NAME}/{TAG_LINE}"
response = httpx.get(url, headers={"X-Riot-Token": API_KEY})

print("status:", response.status_code)
print(response.json())

puuid = response.json()["puuid"]  # take the puuid out of request 1's answer

match_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count=5"
match_response = httpx.get(match_url, headers={"X-Riot-Token": API_KEY})

print("status:", match_response.status_code)
print(match_response.json())
