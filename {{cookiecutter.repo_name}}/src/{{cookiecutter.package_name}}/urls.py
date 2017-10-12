from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = (
    url(r'^wip/$', TemplateView.as_view(template_name='wip.html')),
)
