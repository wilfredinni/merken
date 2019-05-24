from rest_framework import viewsets, permissions

from .serializers import SiteConfigSerializer, HomeMsgSerializer
from .permissions import IsAdminOrReadOnly
from ..models import SiteConfiguration, HomeMsg


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
