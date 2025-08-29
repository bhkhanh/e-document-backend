from django.apps import AppConfig


class DocumentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.document"
    label = "document"
    verbose_name = "Văn bản"
    verbose_name_plural = "Văn bản"
