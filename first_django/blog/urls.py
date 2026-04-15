from django.urls import path
from blog.views import about, home

urlpatterns = [
    path("", home, name="blog-home"),
    path("about/", about, name="blog-about")
    ]
