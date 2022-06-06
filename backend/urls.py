from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # App
    path("", include("app.urls.urls", namespace="app")),
]
