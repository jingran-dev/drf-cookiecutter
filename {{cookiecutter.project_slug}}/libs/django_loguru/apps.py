from django.apps import AppConfig

from libs.django_loguru.setup import setup_logging


class DjangoLoguruConfig(AppConfig):
    name = "libs.django_loguru"

    def ready(self):
        setup_logging()
