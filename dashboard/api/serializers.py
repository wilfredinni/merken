from rest_framework import serializers

from blog.models import Article
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Associate a user with his own articles"""

    articles = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Article.objects.all()
    )

    class Meta:
        model = CustomUser
        fields = ("id", "username", "articles", "github", "twitter", "website", "about")


class ArticleSerializer(serializers.ModelSerializer):
    """All articles with all of his fields."""

    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        fields = "__all__"
