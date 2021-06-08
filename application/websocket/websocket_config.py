import asyncio
import logging
import websockets
from websockets import WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects.')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects.')

    async def send_to_clients(self, message):
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

    async def ws_handler(self, ws: WebSocketServerProtocol, uri: str):
        print('ws message', ws.Data)
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            await self.send_to_clients(message)
