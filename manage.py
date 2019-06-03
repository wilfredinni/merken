import os
import sys
from conf.settings.base import env


if __name__ == "__main__":
    # test, develop or production
    debug = env.bool("DEBUG", default=True)
    if "test" in sys.argv:
        settings_file = "test_ci"
    elif debug:
        settings_file = "dev"
    elif debug is False:
        settings_file = "prod"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings." + settings_file)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
