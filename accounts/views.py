from django.contrib.auth import get_user_model
from rest_framework import status
# from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts import serializers

User = get_user_model()


class LoginView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer: serializers.RegisterSerializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        user: User = serializer.create(validated_data=serializer.validated_data)
        token = serializers.CustomTokenObtainPairSerializer.get_token(user)

        return Response(
            {
                "refresh": str(token),
                "access": str(token.access_token),
            },
            status=status.HTTP_201_CREATED,
        )


# class UserWithPostsView(ListAPIView):
#     queryset = User.objects.all().prefetch_related("posts")
#     serializer_class = serializers.UserWithPostsSerializer


# class UserWithPostAndCategoriesView(ListAPIView):
#     queryset = User.objects.all().prefetch_related("posts__categories")
#     serializer_class = serializers.UserWithPostsAndCategoriesSerializer
