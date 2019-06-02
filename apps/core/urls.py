from django.urls import path

from . import views


urlpatterns = [
    path("", views.DashboardView, name="dashboard"),
]
