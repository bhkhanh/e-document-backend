from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.account"
    label = "account"
    verbose_name = "Tài khoản người dùng"
    verbose_name_plural = "Tài khoản người dùng"
