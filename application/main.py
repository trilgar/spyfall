import asyncio
from application.websocket.websocket_config import Server
import websockets


server = Server()
start_server = websockets.serve(server.ws_handler, 'localhost', 4000)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
