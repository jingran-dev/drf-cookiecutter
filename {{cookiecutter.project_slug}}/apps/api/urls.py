from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api import views

app_name = "api"

router = DefaultRouter()
# Register your viewsets here
# router.register("users", views.UserViewSet)

urlpatterns = [
    # Add your API endpoints here
    path("health/", views.HealthCheckView.as_view(), name="health-check"),
]

urlpatterns += router.urls
