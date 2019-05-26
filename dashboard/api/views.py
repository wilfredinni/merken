from rest_framework import viewsets, permissions, mixins

from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly
from .serializers import (
    SiteConfigSerializer,
    HomeMsgSerializer,
    UserSerializer,
    PageSerializer,
)

from ..models import SiteConfiguration, HomeMsg
from users.models import CustomUser
from pages.models import Page


class ConfigViewSet(viewsets.ModelViewSet):
    # only admin users can update the fields in the SiteConfiguration model
    # authenticated users have safe access to the site configuration endpoint
    # this is so I can display the site information on the dashboard (like site_name)
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigSerializer
    http_method_names = ["get", "put", "head"]


class HomeViewSet(viewsets.ModelViewSet):
    # only admin users can update the fields in the HomeMsg model
    # authenticated users have safe access to the HomeMsg endpoint
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = HomeMsg.objects.all()
    serializer_class = HomeMsgSerializer
    http_method_names = ["get", "put", "head"]


class PagesViewSet(viewsets.ModelViewSet):
    # only admin users can create or update Pages
    # authenticated users have safe access to the PagesViewSet endpoint
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class UserListView(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    # only admin users can create new users
    # authenticated users have safe access to the UsersList endpoint
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    # only admin users or owners can update profiles
    # authenticated users have safe access to the UsersDetail endpoint
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdminOrReadOnly)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
