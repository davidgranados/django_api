from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from halo import Halo

User = get_user_model()


class Command(BaseCommand):
    help = "Inserting data into many to many"
    faker = Faker()

    def _create_user_and_insert_posts(self):
        """
        create a user and save it then inserts many posts for the created user
        and for reach post we need to create many categories
        """

        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self.faker.email()

        user: User = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password="testpass123",
        )

        self._create_posts(u=user)

    def _create_posts(self, u: User):
        from posts.models import CategoryPost, Post
        from categories.factories import CategoryFactory

        categories_id = [c.id for c in CategoryFactory.create_batch(2)]

        for _ in range(1):
            p: Post = Post.objects.create(
                body=self.faker.paragraph(),
                user_id=u.id,
            )

            data = [
                CategoryPost(post_id=p.id, category_id=c_id) for c_id in categories_id
            ]

            CategoryPost.objects.bulk_create(data)

    @Halo(
        text="Inserting data into one to many",
        spinner="dots",
        color="blue",
        text_color="blue",
    )
    @transaction.atomic
    def handle(self, *args, **options):
        self._create_user_and_insert_posts()
