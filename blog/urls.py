from django.urls import path

from . import views

app_name = "blog_app"
urlpatterns = [
    path("blog/", views.blog, name="blog"),
    path("blog/<str:url>/", views.article, name="article"),
    path("blog/tag/<str:tag_name>/", views.article_by_tag, name="tag"),
    ]
