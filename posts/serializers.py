from rest_framework.serializers import ModelSerializer

from categories.serializers import CategorySerializer

from posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "body", "created_at", "updated_at"]


class PostWithCategoriesSerializer(ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "body", "created_at", "updated_at", "categories"]
