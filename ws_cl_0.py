import asyncio
import websockets


async def receive_data():
    async with websockets.connect("ws://37.230.192.239:8080", ping_interval=None) as websocket:
        async for message in websocket:
            print("Received:", message)


async def main():
    await receive_data()


if __name__ == "__main__":
    asyncio.run(main())
