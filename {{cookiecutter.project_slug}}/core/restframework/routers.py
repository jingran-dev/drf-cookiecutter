from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter


def get_router():
    return DefaultRouter() if settings.DEBUG else SimpleRouter()
