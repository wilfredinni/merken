from rest_framework import viewsets, permissions, mixins

from .permissions import (
    IsAdminOrReadOnly,
    IsOwnerOrAdminOrReadOnly,
    IsAuthorOrAdminOrReadOnly,
)
from .serializers import (
    SiteConfigSerializer,
    HomeMsgSerializer,
    UserSerializer,
    FullBlogSerializer,
    AuthorBlogSerializer,
    TagsSerializer,
    PageSerializer,
)

from ..models import SiteConfiguration, HomeMsg
from users.models import CustomUser
from blog.models import Article, Tag
from pages.models import Page


class ConfigViewSet(viewsets.ModelViewSet):
    # only admin users can update the fields in the SiteConfiguration model
    # authenticated users have safe access to the site configuration endpoint
    # this is so I can display the site information on the dashboard (like site_name)
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigSerializer
    http_method_names = ["get", "put", "head"]


class HomeMsgViewSet(viewsets.ModelViewSet):
    # only admin users can update the fields in the HomeMsg model
    # authenticated users have safe access to the HomeMsg endpoint
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = HomeMsg.objects.all()
    serializer_class = HomeMsgSerializer
    http_method_names = ["get", "put", "head"]


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


class ArticlesListView(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    # all authenticated users have access to the Articles endpoint
    # all authenticated users can create new articles
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullBlogSerializer
        return AuthorBlogSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticlesDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    # admin users can update all the articles
    # authors can update only their own articles
    # authenticated users have safe access
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrAdminOrReadOnly)
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullBlogSerializer
        return AuthorBlogSerializer


class TagsViewSet(viewsets.ModelViewSet):
    # only admin users can create or update Tags
    # authenticated users have safe access to the tags endpoint
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class PagesViewSet(viewsets.ModelViewSet):
    # only admin users can create or update Pages
    # authenticated users have safe access to the PagesViewSet endpoint
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = Page.objects.all()
    serializer_class = PageSerializer
