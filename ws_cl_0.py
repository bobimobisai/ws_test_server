import asyncio
import websockets
import random


async def connect_to_server():
    async with websockets.connect("ws://37.230.192.239:8080") as websocket:
        while True:
            response = await websocket.recv()
            print(f"Received: {response}")


asyncio.run(connect_to_server())
