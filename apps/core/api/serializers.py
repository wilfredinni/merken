from rest_framework import serializers

from ..models import SiteConfiguration, HomeMsg
from apps.users.models import CustomUser
from apps.blog.models import Article, Tag
from apps.pages.models import Page


class SiteConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteConfiguration
        fields = "__all__"


class HomeMsgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeMsg
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "url",
            "username",
            "email",
            "password",
            "twitter",
            "github",
            "website",
            "about",
            "articles"
        )
        read_only_fields = ("articles",)
        extra_kwargs = {
            'password': {'write_only': True},
        }


class FullBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class AuthorBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = (
            "url",
            "author",
            "title",
            "overview",
            "content",
            "img_url",
            "tags",
            "slug",
            "allow_comments",
            "is_draft",
            "is_featured",
        )
        read_only_fields = ("is_featured", "author")


class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"
        read_only_fields = ("created_at",)
