from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    IntegerField,
    ModelSerializer,
    Serializer,
    SerializerMethodField,
)

from posts.models import Post

User = get_user_model()


class PostBasicUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class PostWithUserSerializer(ModelSerializer):
    user = PostBasicUserSerializer()

    class Meta:
        model = Post
        fields = ["id", "body", "user"]


class PostWithCategoriesCountSerializer(ModelSerializer):
    categories_count = SerializerMethodField()
    user = PostBasicUserSerializer()

    def get_categories_count(self, obj):
        return obj.categories_count

    class Meta:
        model = Post
        fields = ["id", "body", "categories_count", "user"]


class PostGroupByCreatedDaySerializer(Serializer):
    count = IntegerField()
    created_day = IntegerField()
