from django.urls import path
from .views import blog_Details
urlpatterns = [
    path('', blog_Details, name='blog_details'),
]