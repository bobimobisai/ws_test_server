import asyncio
import websockets
import random


def gen():
    yield random.randint(1, 10000)


async def connect_to_server():
    async with websockets.connect("ws://37.230.192.239:8080", ping_interval=None) as websocket:
        while True:
            for i in gen():
                await websocket.send(str(i))


asyncio.run(connect_to_server())
