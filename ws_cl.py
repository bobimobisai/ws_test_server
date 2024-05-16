import asyncio
import websockets
import random


def gen():
    yield random.randint(1, 10000)


async def connect_to_server():
    async with websockets.connect("ws://37.230.192.239:8080", ping_interval=None) as websocket:
        while True:
            g = next(gen())
            await websocket.send(str(g))
            response = await websocket.recv()
            print(f"Received: {response}")


asyncio.run(connect_to_server())
