from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel, SoftDeleteModel
from posts.model_enums import Weight

User = get_user_model()


class Post(BaseModel, SoftDeleteModel):
    body = models.TextField(null=False)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    categories = models.ManyToManyField("categories.Category", through="CategoryPost")


# https://docs.djangoproject.com/en/3.2/ref/models/fields/
class CategoryPost(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE)
    weight = models.ForeignKey("categories.CategoryWeight", on_delete=models.PROTECT)

    class Meta:
        unique_together = [["post_id", "category_id"]]
