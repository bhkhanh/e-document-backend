from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.category"
    label = "category"
    verbose_name = "Danh mục phân loại"
    verbose_name_plural = "Danh mục phân loại"
