import random
from factory import SubFactory, fuzzy, RelatedFactoryList
from factory.django import DjangoModelFactory
from factory.faker import Faker

from categories.factories import Weight


class CategoryPostFactory(DjangoModelFactory):
    post = SubFactory("posts.factories.PostFactory")
    weight = SubFactory("categories.factories.CategoryWeightFactory")
    category = SubFactory("categories.factories.CategoryFactory")

    class Meta:
        model = "posts.CategoryPost"
        # because the category is selected randomly
        django_get_or_create = ["category", "post"]


class PostFactory(DjangoModelFactory):
    body = Faker("paragraph")
    user = SubFactory("accounts.factories.UserFactory")

    categories = RelatedFactoryList(
        CategoryPostFactory,
        factory_related_name="post",
        size=lambda: random.randint(1, 5),
    )

    class Meta:
        model = "posts.Post"
