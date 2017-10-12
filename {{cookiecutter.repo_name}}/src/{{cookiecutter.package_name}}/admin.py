# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from django.contrib.admin import ModelAdmin, site
from .models import *

{% if cookiecutter.model_name %}class {{cookiecutter.model_name}}Admin(ModelAdmin):
    pass

site.register({{cookiecutter.model_name}}, {{cookiecutter.model_name}}Admin){% endif %}
