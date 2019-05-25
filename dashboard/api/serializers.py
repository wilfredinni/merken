from rest_framework import serializers

from ..models import SiteConfiguration, HomeMsg
from users.models import CustomUser


class SiteConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteConfiguration
        fields = "__all__"


class HomeMsgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeMsg
        fields = "__all__"


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    # articles = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Article.objects.all()
    # )

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            "twitter",
            "github",
            "website",
            "about",
            # "articles"
        )
