import asyncio
import time
import httpx
from riot_api import HEADERS, get_puuid, get_match_ids, get_match


async def get_match_async(
    client: httpx.AsyncClient, match_id: str, sem: asyncio.Semaphore, start: float
) -> dict:
    async with sem:
        url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}"
        while True:
            response = await client.get(url, headers=HEADERS)

            if response.status_code == 200:  # success?
                return response.json()

            if response.status_code == 429:  # rate limited?
                wait = int(response.headers["Retry-After"])
                print(f"429! waiting {wait}s before retrying {match_id}")
                await asyncio.sleep(wait)  # wait, the async way

            else:
                response.raise_for_status()  # any other error: stop with a clear message


async def main():
    puuid = get_puuid(
        "KoKayn", "Vycka"
    )  # still one by one: each needs the previous answer
    ids = get_match_ids(puuid, 20)

    # start = time.perf_counter()

    # slow = [get_match(mid) for mid in ids]  # one by one, the old way
    # print(
    #    f"one by one: {len(slow)} matches in {time.perf_counter() - start:.2f} seconds"
    # )

    start = time.perf_counter()
    sem = asyncio.Semaphore(5)
    async with httpx.AsyncClient() as client:
        matches = await asyncio.gather(
            *[get_match_async(client, mid, sem, start) for mid in ids]
        )
    print(f"async: {len(matches)} matches in {time.perf_counter() - start:.2f} seconds")


asyncio.run(main())
