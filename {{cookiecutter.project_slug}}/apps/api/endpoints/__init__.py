from django.urls import include, path

app_name = "api"


endpoints = [
    path("", include("apps.api.endpoints.v1")),
]

urlpatterns = [
    path("api/", include(endpoints)),
]
