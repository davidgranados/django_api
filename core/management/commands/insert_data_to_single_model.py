from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from halo import Halo
from factory.faker import Faker

User = get_user_model()


class Command(BaseCommand):

    help = "Inserting data into a single model"
    faker = Faker()

    def _get_last_user_id(self):
        return User.objects.last().id

    def _way_1(self):
        """
        Save the post directly to the db and return an instance for it.
        """

        from posts.models import Post

        new_post: Post = Post.objects.create(
            body=self.faker.paragraph(), user_id=self._get_last_user_id()
        )
        # new_post.refresh_from_db()
        return new_post

    def _way_2(self):
        from posts.models import Post

        temp_post: Post = Post(
            body=self.faker.paragraph(), user_id=self._get_last_user_id()
        )

        # print(temp_post.id)  # None
        temp_post.save()
        # print(temp_post.id)  # number after save

    @Halo(
        text="Inserting data into a single model",
        spinner="dots",
        color="blue",
        text_color="blue",
    )
    def handle(self, *args, **options):
        self._way_1()
        self._way_2()
