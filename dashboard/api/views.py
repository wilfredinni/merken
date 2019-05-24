from rest_framework import generics
from rest_framework import permissions

from blog.models import Article
from users.models import CustomUser

from .serializers import ArticleSerializer, UserSerializer


class UserList(generics.ListAPIView):
    """A list of all the users and his articles."""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """A user detail"""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ArticlesListView(generics.ListCreateAPIView):
    """View and create articles."""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticlesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View, create and delete an article."""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
