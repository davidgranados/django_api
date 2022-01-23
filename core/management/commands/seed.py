from halo import Halo
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from accounts.factories import UserFactory
from categories.factories import CategoryFactory, CategoryNames
# from posts.factories import PostFactory


class Command(BaseCommand):
    help = "Generate fake data and seed the models with them, defailt are 10"

    def add_arguments(self, parser):
        # https://docs.python.org/3/library/argparse.html#the-add-argument-method
        parser.add_argument("--qty", type=int, help="The quantity of fake date you want." )


    def _generate_users(self, qty):
        UserFactory.create_batch(qty)

        # PostFactory.create_batch(qty)

        # for key, _ in CategoryNames.choices:
        #     CategoryFactory.create(name=key)
        
        # for _ in range(qty):
        #     UserFactory()

    @Halo(text="Generating...", spinner="dots", color="blue", text_color="blue")
    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")
        qty = options.get("qty") or 10
        self._generate_users(qty)
