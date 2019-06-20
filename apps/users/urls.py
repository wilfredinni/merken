from django.urls import path

from . import views

app_name = "users_app"
urlpatterns = [path("author/<str:slug>", views.ProfileView.as_view(), name="profile")]
