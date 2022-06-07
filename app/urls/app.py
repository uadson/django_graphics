from django.urls import path

from app.views.index import IndexView
from app.views.data import DataJSONView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("data/", DataJSONView.as_view(), name="data"),
]
