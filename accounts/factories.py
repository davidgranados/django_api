import random
from django.contrib.auth import get_user_model
from factory import PostGenerationMethodCall, RelatedFactoryList, sequence
from factory.django import DjangoModelFactory
from factory.faker import Faker

User = get_user_model()


class UserFactory(DjangoModelFactory):
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    password = PostGenerationMethodCall("set_password", "secret")
    
    posts = RelatedFactoryList("posts.factories.PostFactory", "user", size=lambda: random.randint(1, 5))

    # email = Faker("email")
    @sequence
    def email(n):
        try:
            max_id = User.objects.latest("pk").pk
            return f"user-{max_id + 1}@example.xyz"
        except User.DoesNotExist:
            return f"user-0@example.xyz"

    class Meta:
        model = "accounts.User"
        django_get_or_create = ["email"]
