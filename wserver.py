import asyncio
import websockets
import random

cl_list = []


async def send_message(message: str):
    for client in cl_list:
        await client.send(str(message))


async def new_client(cl_soket: websockets.WebSocketClientProtocol, path: str):
    cl_list.append(cl_soket)
    async for new_message in cl_soket:
        for client in cl_list:
            if client != cl_soket:
                await client.send(new_message)


async def start_server():
    async with websockets.serve(new_client, "0.0.0.0", 8080, ping_interval=None):
        await asyncio.Future()


async def main():
    await asyncio.gather(start_server())


if __name__ == "__main__":
    asyncio.run(main())
