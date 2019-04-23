from django.core.management.base import BaseCommand
from merken.settings.base import BASE_DIR


# TODO: auto generate SECRET_KEY
# TODO: DRY

ENV_FIELDS = {
    "common": ["SECRET_KEY", "DEBUG"],
    "dev": ["DEV_DB_NAME", "DEV_DB_USERNAME"],
    "prod": ["DB_NAME", "DB_USERNAME", "DB_PASSWORD", "DB_HOST"],
}


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

        def create_env_file(settings):
            with open(BASE_DIR + "/.env", "w") as e:
                e.write(settings)

        def development():
            secret_key = input("SECRET_KEY: ")
            dev_db_name = input("DEV DB NAME: ")
            dev_db_username = input("DEV DB USERNAME: ")

            env_file = (
                "DEBUG=True\n"
                f"SECRET_KEY={secret_key}\n\n"
                f"DEV_DB_NAME={dev_db_name}\n"
                f"DEV_DB_USERNAME={dev_db_username}"
            )
            # print(env_file)
            create_env_file(env_file)

        def production():
            secret_key = input("SECRET_KEY: ")
            db_username = input("DB NAME: ")
            db_username = input("DB USERNAME: ")
            db_password = input("DB PASSWORD: ")
            db_host = input("DB HOST: ")

            env_file = (
                "DEBUG=False\n"
                f"SECRET_KEY={secret_key}\n\n"
                f"DB_NAME={db_username}\n"
                f"DB_USERNAME={db_username}\n"
                f"DB_PASSWORD={db_password}\n"
                f"DB_HOST={db_host}"
            )
            # print(env_file)
            create_env_file(env_file)

        def both():
            # commons
            debug = input("DEBUG: ")
            secret_key = input("SECRET_KEY: ")

            # development
            dev_db_name = input("DEV DB NAME: ")
            dev_db_username = input("DEV DB USERNAME: ")

            # production
            db_username = input("DB NAME: ")
            db_username = input("DB USERNAME: ")
            db_password = input("DB PASSWORD: ")
            db_host = input("DB HOST: ")

            env_file = (
                # common
                f"DEBUG={debug}\n"
                f"SECRET_KEY={secret_key}\n\n"
                # development
                f"DEV_DB_NAME={dev_db_name}\n"
                f"DEV_DB_USERNAME={dev_db_username}\n\n"
                # production
                f"DB_NAME={db_username}\n"
                f"DB_USERNAME={db_username}\n"
                f"DB_PASSWORD={db_password}\n"
                f"DB_HOST={db_host}"
            )
            create_env_file(env_file)

        if env_for == "dev":
            development()
        elif env_for == "prod":
            production()
        elif env_for == "both":
            both()
        else:
            print("Wrong Option: Choose between 'dev', 'prod' or 'both'.")
