from django.urls import include, path

app_name = "api"


apis = [
    path("", include("apps.api.endpoints.v1")),
]

urlpatterns = [
    path("api/", include(apis)),
]
