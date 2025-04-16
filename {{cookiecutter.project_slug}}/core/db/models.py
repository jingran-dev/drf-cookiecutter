from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.db.mixins import SoftDeleteMixin


class BaseModel(models.Model):
    """
    Base model class that provides common fields and functionality for all models.
    This model does NOT include soft delete functionality.

    Fields:
        created_at: When the record was created
        updated_at: When the record was last updated
    """

    # Database Fields
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        default=timezone.now,
        editable=False,
        help_text=_("When this record was created"),
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True,
        help_text=_("When this record was last updated"),
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]
        get_latest_by = "created_at"

    def save(self, *args, **kwargs):
        """
        Override save method to update updated_at timestamp
        """
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class SoftDeleteBaseModel(SoftDeleteMixin, BaseModel):
    """
    Base model class that provides common fields and functionality for all models,
    including soft delete functionality.

    Fields:
        created_at: When the record was created (from BaseModel)
        updated_at: When the record was last updated (from BaseModel)
        is_deleted: Soft deletion flag (from SoftDeleteMixin)
    """

    class Meta(BaseModel.Meta):
        abstract = True
