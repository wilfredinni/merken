from rest_framework import viewsets, permissions

from .serializers import SiteConfigSerializer, HomeMsgSerializer
from ..models import SiteConfiguration, HomeMsg


class ConfigViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigSerializer


class HomeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = HomeMsg.objects.filter(id=1)
    serializer_class = HomeMsgSerializer
