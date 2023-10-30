# from django.urls import re_path

# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/notification/(?P<room_name>\w+)/$', consumers.NotificationConsumer.as_asgi()),
# ]
# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
# from myapp.consumers import YourConsumer
from . import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        re_path("ws/notification/broadcast/", consumers.NotificationConsumer.as_asgi()),
    ]),
})
