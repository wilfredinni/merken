from django.urls import path

from . import views

app_name = "blog_app"
urlpatterns = [
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("blog/<str:slug>/", views.ArticleView.as_view(), name="article"),
    path("blog/tag/<str:tag_name>/", views.article_by_tag, name="tag"),
    ]
