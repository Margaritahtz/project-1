from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path
from base import consumers
import FYP.routing

websocket_urlPattern = [
    path('ws/polData/',consumers.DashConsumer.as_asgi()),
]


application = ProtocolTypeRouter({

'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))

})


