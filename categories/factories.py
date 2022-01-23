from django.db.models import TextChoices
from factory import fuzzy
from factory.django import DjangoModelFactory


class CategoryNames(TextChoices):
    GENERAL = "general"
    JAVASCRIPT = "javascript"
    PYTHON = "python"
    RUBY = "ruby"
    PHP = "php"


class Weight(TextChoices):
    IMPORTANT = "important"
    LITTLE = "little"
    KINDA_RELATES = "kinda_relates"


class CategoryWeightFactory(DjangoModelFactory):
    name = fuzzy.FuzzyChoice(Weight)

    class Meta:
        model = "categories.CategoryWeight"
        django_get_or_create = ["name"]


class CategoryFactory(DjangoModelFactory):
    name = fuzzy.FuzzyChoice(CategoryNames)

    class Meta:
        model = "categories.Category"
        django_get_or_create = ["name"]



