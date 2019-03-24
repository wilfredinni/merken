from django.urls import path

from . import views
from .feed import ArticleFeed

app_name = "blog_app"
urlpatterns = [
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("blog/<str:slug>/", views.ArticleView.as_view(), name="article"),
    path("blog/tag/<str:slug>/", views.TagView.as_view(), name="tag"),
    path("latest/feed/", ArticleFeed(), name='rss_feed'),
]
