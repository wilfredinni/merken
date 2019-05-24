from rest_framework import viewsets, permissions

from .serializers import SiteConfigSerializer, HomeMsgSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly
from ..models import SiteConfiguration, HomeMsg
from users.models import CustomUser


class ConfigViewSet(viewsets.ModelViewSet):
    # only authenticated users can have access to the site configuration endpoint
    # only admin users can update the fields in the SiteConfiguration model
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly,)
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigSerializer


class HomeViewSet(viewsets.ModelViewSet):
    # only authenticated users can have access to the HomeMsg endpoint
    # only admin users can update the fields in the HomeMsg model
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly,)
    queryset = HomeMsg.objects.all()
    serializer_class = HomeMsgSerializer


class UserViewSet(viewsets.ModelViewSet):
    # only authenticated users can have access to the HomeMsg endpoint
    # only admin users can update the fields in the HomeMsg model
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
