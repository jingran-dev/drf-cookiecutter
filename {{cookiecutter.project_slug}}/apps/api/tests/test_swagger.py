from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_swagger_accessible(client):
    url = reverse("api:api-docs")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_api_schema_generated_successfully(client):
    url = reverse("api:api-schema")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
