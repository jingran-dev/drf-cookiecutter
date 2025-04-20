from django.urls import include, path
from apps.api import views
from core.restframework.routers import get_router

router = get_router()

urlpatterns = [
    path("health/", views.HealthCheckView.as_view(), name="health-check"),
    path("", include(router.urls)),
]
