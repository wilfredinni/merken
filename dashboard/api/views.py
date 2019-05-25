from rest_framework import viewsets, permissions, mixins

from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly
from .serializers import SiteConfigSerializer, HomeMsgSerializer, UserSerializer

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


class UserListView(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    # only authenticated users can have access to the Users endpoint
    # only admin users can create new users
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    # only authenticated users can have access to the Users Details endpoint
    # only admin users or owners can update profiles
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdminOrReadOnly)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
