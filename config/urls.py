"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Admin:
    path(route="admin/", view=admin.site.urls),
    # API documentation:
    path(route="schema/json/", view=SpectacularJSONAPIView.as_view(), name="schema"),
    path(route="docs/", view=SpectacularSwaggerView.as_view(url_name="schema")),
    # Application:
    path(route="account/", view=include("app.account.urls")),
    path(route="category/", view=include("app.category.urls")),
    path(route="document/", view=include("app.document.urls")),
]


# Override some AdminSite attributes to customize the default admin site
# See https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#adminsite-objects
admin.AdminSite.empty_value_display = "-----"
admin.AdminSite.site_header = "E-document"
admin.AdminSite.site_title = "E-document"
admin.AdminSite.index_title = "Administration"
