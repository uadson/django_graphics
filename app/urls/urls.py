from django.urls import path, include

from . import app


app_name = "app"

urlpatterns = [
    path("", include(app)),
]
