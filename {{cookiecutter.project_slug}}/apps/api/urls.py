from django.conf import settings
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from apps.api import views
from core.restframework.routers import get_router

app_name = "api"

router = get_router()
# Register your viewsets here
# router.register("users", views.UserViewSet)

urlpatterns = [
    # Add your API endpoints here
    path("health/", views.HealthCheckView.as_view(), name="health-check"),
]

# API Documentation URLs - only added if SHOW_API_DOCS is True
if settings.SHOW_API_DOCS:
    urlpatterns += [
        # API Schema
        path("schema/", SpectacularAPIView.as_view(), name="api-schema"),
        # Swagger UI
        path(
            "docs/",
            SpectacularSwaggerView.as_view(url_name="api:api-schema"),
            name="api-docs",
        ),
        # ReDoc UI
        path(
            "redoc/",
            SpectacularRedocView.as_view(url_name="api:api-schema"),
            name="api-redoc",
        ),
    ]

urlpatterns += router.urls
