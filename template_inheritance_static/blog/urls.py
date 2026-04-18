from django.urls import path
from .views import home, about, submit_post

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('submit/', submit_post, name='submit_post'),
]