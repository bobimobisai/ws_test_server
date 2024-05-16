import asyncio
import websockets
import random

def gen():
    yield random.randint(1, 10000)


async def connect_to_server():
    async with websockets.connect("ws://localhost:8080") as websocket:
        while True:
            g = next(gen())
            await websocket.send(str(g))
            response = await websocket.recv()
            print(f"Received: {response}")

asyncio.run(connect_to_server())
