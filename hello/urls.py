from django.urls import path

from.views import send_json

urlpatterns = [
    path("", send_json, name="home"),
]