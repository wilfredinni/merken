from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("blog.urls")),
    path("", include("users.urls")),
    path("", include("pages.urls")),

    path("admin/", admin.site.urls),
    ]
