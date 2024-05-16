import asyncio
import random
import websockets

clients = []


async def send_data():
    while True:
        # Генерируем случайные цифры для кортежа
        data = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))
        # Преобразуем кортеж в строку для отправки
        message = ",".join(map(str, data))
        # Отправляем сообщение всем клиентам
        await asyncio.wait([client.send(message) for client in clients])
        # Ждем некоторое время перед отправкой следующего сообщения
        # await asyncio.sleep(1)


async def new_client(websocket, path):
    clients.append(websocket)
    async for message in websocket:
         # При получении сообщения от клиента можно выполнить какие-то действия
        pass


async def start_server():
    # Запускаем сервер на порту 8080
    async with websockets.serve(new_client, "0.0.0.0", 8080):
        # Запускаем бесконечный цикл отправки данных
        await asyncio.gather(send_data())


asyncio.run(start_server())
