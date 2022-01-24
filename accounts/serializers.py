from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from posts.models import Post
from categories.models import Category

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["email"] = user.email
        token["user_id"] = user.pk

        return token


class RegisterSerializer(ModelSerializer):
    password_confirmation = CharField(required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "password",
            "password_confirmation",
            "email",
        )
        extra_kwargs = {
            "first_name": {"required": True, "allow_blank": False},
            "last_name": {"required": True, "allow_blank": False},
        }

    def validate(self, data):
        if data["password"] != data["password_confirmation"]:
            raise ValidationError({"error_message": _("Passwords do not match")})
        return data

    def create(self, validated_data):
        user: User = User.objects.create_user(
            email=validated_data.get("email"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            password=validated_data.get("password"),
        )
        return user


class UserCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "body", "created_at", "updated_at"]


class UserPostWithCategoriesSerializer(ModelSerializer):
    categories = UserCategorySerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "body", "created_at", "updated_at", "categories"]


class UserWithPostsSerializer(ModelSerializer):
    posts = UserPostSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "posts"]


class UserWithPostsAndCategoriesSerializer(ModelSerializer):
    posts = UserPostWithCategoriesSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "posts"]


class UsersWithPostCountSerializer(ModelSerializer):
    posts_count = SerializerMethodField()

    def get_posts_count(self, obj):
        return obj.posts_count

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "posts_count"]
