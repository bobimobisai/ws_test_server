import asyncio
import logging
import websockets

cl_list = []


async def send_message(message: str):
    for client in cl_list:
        await client.send(str(message))


async def new_client(cl_soket: websockets.WebSocketClientProtocol, path: str):
    cl_list.append(cl_soket)
    while True:
        new_message = await cl_soket.recv()
        await send_message(message=new_message)


async def start_server():
    await websockets.serve(new_client, "0.0.0.0", 8080)


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()
