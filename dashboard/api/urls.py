from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "api"

urlpatterns = [
    path("articles/", views.ArticlesListView.as_view()),
    path("articles/<int:pk>/", views.ArticlesDetailView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)