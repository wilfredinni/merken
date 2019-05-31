from django.urls import path

from . import views


urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    # path("", views.DashboardView, name="dashboard"),
]
