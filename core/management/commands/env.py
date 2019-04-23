from django.core.management.base import BaseCommand
from merken.settings.base import BASE_DIR


class Command(BaseCommand):
    help = "Creates a .env file for Development or Production, or both."

    def add_arguments(self, parser):
        parser.add_argument(
            "env_file_for",
            type=str,
            help="Create a .env file for 'dev', 'prod' or 'both'.",
        )

    def handle(self, *args, **kwargs):
        env_for = kwargs["env_file_for"]

        def create_env_file():
            with open(BASE_DIR + "/.env", 'w') as e:
                pass

        def development():
            create_env_file()

        def production():
            print("production")

        def both():
            print("both")

        if env_for == "dev":
            development()
        elif env_for == "prod":
            production()
        elif env_for == "both":
            both()
        else:
            print("Wrong Option: Choose between 'dev', 'prod' or 'both'.")
