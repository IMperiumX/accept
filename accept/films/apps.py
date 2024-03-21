import contextlib

from django.apps import AppConfig


class FilmsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accept.films"

    def ready(self):
        with contextlib.suppress(ImportError):
            import accept.films.signals  # noqa: F401
