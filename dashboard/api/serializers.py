from rest_framework import serializers

from ..models import SiteConfiguration, HomeMsg
# from blog.models import Article
from users.models import CustomUser


class SiteConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteConfiguration
        fields = "__all__"


class HomeMsgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeMsg
        fields = "__all__"


class UserAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "url",
            "username",
            "email",
            "password",
        )


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    # articles = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Article.objects.all()
    # )

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
        # read_only_fields = ("articles",)
