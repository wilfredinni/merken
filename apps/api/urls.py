from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# site configuration
router.register(r"configuration", views.ConfigViewSet)
router.register(r"message", views.HomeMsgViewSet)

# users Detail and ListView
router.register(r"users", views.UserListView)
router.register(r"users", views.UserDetailView)

# articles and tags, Detail and ListView
router.register(r"articles", views.ArticlesListView)
router.register(r"articles", views.ArticlesDetailView)
router.register(r"tags", views.TagsViewSet)

# pages
router.register(r"pages", views.PagesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
