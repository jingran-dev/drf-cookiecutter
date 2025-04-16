from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.db.managers import ActiveManager, AllObjectsManager


class SoftDeleteMixin(models.Model):
    """
    Mixin that provides soft deletion functionality for models.

    Fields:
        is_deleted: Soft deletion flag
    """

    # Database Fields
    is_deleted = models.BooleanField(
        verbose_name=_("Deleted"),
        default=False,
        help_text=_("Whether this record is deleted"),
    )

    # Managers
    objects = ActiveManager()  # Default manager, only returns non-deleted records
    all_objects = AllObjectsManager()  # Returns all records including deleted ones

    class Meta:
        abstract = True

    def delete(self, *, using=None, keep_parents: bool = False):
        """
        Soft delete the model instance by setting is_deleted=True.
        To perform a hard delete, use Model.objects.filter(pk=id).delete()
        """
        self.is_deleted = True
        self.save(using=using)

    def hard_delete(self, *, using=None, keep_parents: bool = False):
        """
        Permanently delete the model instance from the database
        """
        super().delete(using=using, keep_parents=keep_parents)

    def restore(self, *, using=None):
        """
        Restore a soft-deleted instance
        """
        self.is_deleted = False
        self.save(using=using)
