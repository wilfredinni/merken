from django.urls import path

from . import views

app_name = "page_app"
urlpatterns = [
    path("<str:slug>/", views.PageView.as_view(), name="page")
]
