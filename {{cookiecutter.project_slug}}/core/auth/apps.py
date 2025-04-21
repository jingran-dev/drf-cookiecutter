from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthConfig(AppConfig):
    name = "core.auth"
    label = "authentication"  # 使用自定义标签避免与 Django 内置 auth 应用冲突
    verbose_name = _("Authentication")

    def ready(self):
        try:
            import core.auth.signals  # noqa: F401
        except ImportError:
            pass
