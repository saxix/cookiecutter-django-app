from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = (
    url(r'', include("{{ cookiecutter.package_name}}.urls")),
    url(r'^admin/', admin.site.urls),
)
