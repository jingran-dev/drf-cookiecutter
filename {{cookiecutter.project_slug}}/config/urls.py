"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

API_TITLE = "{{ cookiecutter.project_name }} API"
API_DESCRIPTION = "{{ cookiecutter.description }}"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.api.urls")),
    path("api/docs/", include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
