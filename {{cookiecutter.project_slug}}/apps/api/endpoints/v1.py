from django.urls import include, path

from apps.api import views

app_name = "v1"

endpoints = [
    path("health/", views.HealthCheckView.as_view(), name="health-check"),
]

urlpatterns = [
    path("v1/", include(endpoints)),
]
