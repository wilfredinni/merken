import os
import secrets
import string
import sys

from django.core.management.base import BaseCommand

from conf.settings.base import BASE_DIR


# TODO: check choice for debug (True/False)
def secret_key():
    return "".join(
        secrets.choice(string.digits + string.ascii_letters + string.punctuation)
        for i in range(100)
    )


ENV_QUESTIONS = {
    # common
    "debug": lambda: input("DEBUG: "),
    "secret_key": lambda: secret_key(),
    # development
    "dev_db_name": lambda: input("DEV_DB_NAME: "),
    "dev_db_username": lambda: input("DEV_DB_USERNAME: "),
    # production
    "db_name": lambda: input("DB_NAME: "),
    "db_username": lambda: input("DB_USERNAME: "),
    "db_password": lambda: input("DB_PASSWORD: "),
    "db_host": lambda: input("DB_HOST: "),
    "sentry_dsn": lambda: input("SENTRY_DSN: "),
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

        if os.path.isfile(BASE_DIR + "/.env"):
            choice = input(
                ".env file already exists. Do you want to replace it? [y/n]: "
            )
            if choice == "n":
                sys.exit()
            elif choice != "y":
                print("Unexpected choice.")
                sys.exit()

        def create_env_file(settings):
            with open(BASE_DIR + "/.env", "w") as e:
                e.write(settings)

        def development():
            env_file = (
                "DEBUG=True\n",
                f"SECRET_KEY={ENV_QUESTIONS['secret_key']()}\n\n"
                f"DEV_DB_NAME={ENV_QUESTIONS['dev_db_name']()}\n"
                f"DEV_DB_USERNAME={ENV_QUESTIONS['dev_db_username']()}",
            )
            create_env_file(env_file)

        def production():
            env_file = (
                "DEBUG=False\n"
                f"SECRET_KEY={ENV_QUESTIONS['secret_key']()}\n\n"
                f"DB_NAME={ENV_QUESTIONS['db_name']()}\n"
                f"DB_USERNAME={ENV_QUESTIONS['db_username']()}\n"
                f"DB_PASSWORD={ENV_QUESTIONS['db_password']()}\n"
                f"DB_HOST={ENV_QUESTIONS['db_host']()}\n"
                f"SENTRY_DSN={ENV_QUESTIONS['sentry_dsn']()}"
            )
            create_env_file(env_file)

        def both():
            env_file = (
                # common
                f"DEBUG={ENV_QUESTIONS['debug']()}\n"
                f"SECRET_KEY={ENV_QUESTIONS['secret_key']()}\n\n"
                # development
                f"DEV_DB_NAME={ENV_QUESTIONS['dev_db_name']()}\n"
                f"DEV_DB_USERNAME={ENV_QUESTIONS['dev_db_username']()}\n\n"
                # production
                f"DB_NAME={ENV_QUESTIONS['db_name']()}\n"
                f"DB_USERNAME={ENV_QUESTIONS['db_username']()}\n"
                f"DB_PASSWORD={ENV_QUESTIONS['db_password']()}\n"
                f"DB_HOST={ENV_QUESTIONS['db_host']()}\n"
                f"SENTRY_DSN={ENV_QUESTIONS['sentry_dsn']()}"
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
