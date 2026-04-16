from .views import home, about
from django.urls import path

urlpatterns = [
    path("", home, name="shop-home"),
    path("about/", about, name="shop-about"),
]