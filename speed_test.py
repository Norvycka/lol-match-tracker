import asyncio
import time
import httpx
from riot_api import HEADERS, get_puuid, get_match_ids, get_match


async def get_match_async(
    client: httpx.AsyncClient, match_id: str, sem: asyncio.Semaphore, start: float
) -> dict:
    async with sem:
        print(f"{time.perf_counter() - start:5.2f}s  START {match_id}")
        url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}"
        response = await client.get(url, headers=HEADERS)
        print(f"{time.perf_counter() - start:5.2f}s  done  {match_id}")
        return response.json()


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
    sem = asyncio.Semaphore(10)
    async with httpx.AsyncClient() as client:
        matches = await asyncio.gather(
            *[get_match_async(client, mid, sem, start) for mid in ids]
        )
    print(f"async: {len(matches)} matches in {time.perf_counter() - start:.2f} seconds")


asyncio.run(main())
