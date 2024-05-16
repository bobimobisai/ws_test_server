import asyncio
import websockets

cl_list = []


async def send_message(message: str):
    if cl_list:
        await asyncio.wait([await client.send(message) for client in cl_list])


async def new_client(cl_soket: websockets.WebSocketClientProtocol, path: str):
    cl_list.append(cl_soket)
    try:
        async for new_message in cl_soket:
            await send_message(new_message)
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        cl_list.remove(cl_soket)


async def start_server():
    async with websockets.serve(new_client, "0.0.0.0", 8080, ping_interval=None):
        await asyncio.Future()


async def main():
    await asyncio.gather(start_server())


if __name__ == "__main__":
    asyncio.run(main())
