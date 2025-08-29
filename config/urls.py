from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"schema/", SpectacularJSONAPIView.as_view(), name="schema"),
    path(r"documentation/", SpectacularSwaggerView.as_view(url_name="schema")),
    path(r"account/", include("app.account.urls")),
    path(r"category/", include("app.category.urls")),
    path(r"document/", include("app.document.urls")),
]


# Override some AdminSite attributes to customize the default admin site
# See https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#adminsite-objects
admin.AdminSite.empty_value_display = "---"
admin.AdminSite.site_header = "E-document"
admin.AdminSite.site_title = "E-document"
admin.AdminSite.index_title = "Administration"
