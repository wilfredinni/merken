from rest_framework import viewsets, permissions

from .permissions import IsAdminOrReadOnly, IsSameUserOrReadOnly
from .serializers import (
    SiteConfigSerializer,
    HomeMsgSerializer,
    UserProfileSerializer,
    UserAdminSerializer,
)

from ..models import SiteConfiguration, HomeMsg
from users.models import CustomUser


class ConfigViewSet(viewsets.ModelViewSet):
    # only admin users can update the fields in the SiteConfiguration model
    # authenticated users have access to the site configuration endpoint
    # this is I can display the site information on the dashboard (like site_name)
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigSerializer
    http_method_names = ["get", "put", "head"]


class HomeViewSet(viewsets.ModelViewSet):
    # only authenticated users can have access to the HomeMsg endpoint
    # only admin users can update the fields in the HomeMsg model
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = HomeMsg.objects.all()
    serializer_class = HomeMsgSerializer
    http_method_names = ["get", "put", "head"]


class UserAdminViewSet(viewsets.ModelViewSet):
    # only the admins have access to the UserAdminViewSet endpoint
    # the admin has full permissions
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserAdminSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    # only authenticated users can have access to the UserProfileViewSet endpoint
    # no one, not even the admin can create new users from here
    # only the user can update his user profile
    permission_classes = (permissions.IsAuthenticated, IsSameUserOrReadOnly)
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ["get", "put", "head"]
