from django.db import models

from core.db.models import BaseModel, SoftDeleteBaseModel


class DummyModel(SoftDeleteBaseModel):
    """A test model that inherits from SoftDeleteBaseModel"""

    name = models.CharField(max_length=100)


class RegularModel(BaseModel):
    """A test model that inherits from regular BaseModel without soft delete"""

    name = models.CharField(max_length=100)
