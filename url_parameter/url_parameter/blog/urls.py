from django.urls import path, re_path
from blog.views import article_details, article_year_month, post_details, username_details, home
urlpatterns = [
    path("", home, name="blog-home"),
    path("post/<int:id>/", post_details, name="post-details"),
    path("user/<str:username>/", username_details, name="username-details"),
    path("article_year/<int:year>/<str:month>/", article_year_month, name="article-year-month"),
    re_path(r'^article/(?P<year>[0-9]{4})/$', article_details, name="article-details"),
    ]