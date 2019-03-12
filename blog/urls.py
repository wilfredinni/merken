from django.urls import path

from . import views

app_name = "blogApp"
urlpatterns = [
    path("blog/", views.blog, name="blog"),
    path("blog/article/", views.article, name="article"),
    path("blog/tag/", views.article_by_tag, name="tag"),
    ]
