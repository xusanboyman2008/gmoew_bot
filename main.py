import asyncio
import aiohttp
import time

API_URL = "https://gmeow-api-prod.anomalygames.ai/api/pet-action"
PAYLOAD = {
    "novalink_user_id": "xpr8vltiiwyedff6zuhgwn1n"
}

async def send_forever():
    timeout = aiohttp.ClientTimeout(total=5)
    connector = aiohttp.TCPConnector(limit=0, ssl=False)

    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        count = 0
        while True:
            start = time.time()
            try:
                async with session.post(API_URL, json=PAYLOAD) as response:
                    status = response.status
                    duration = time.time() - start
                    count += 1
                    print(f"#{count} ✅ {status} in {duration*1000:.2f} ms")
            except Exception as e:
                print(f"❌ Error: {e}")

asyncio.run(send_forever())
