from django.apps import AppConfig

from lib.django_loguru.setup import setup_logging


class DjangoLoguruConfig(AppConfig):
    name = "lib.django_loguru"

    def ready(self):
        setup_logging()
