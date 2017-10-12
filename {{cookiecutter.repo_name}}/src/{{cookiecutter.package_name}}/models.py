# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import logging
from django.utils.translation import gettext as _
from django.db import models

logger = logging.getLogger(__name__)

{% if cookiecutter.model_name %}class {{cookiecutter.model_name}}(models.Model):
    class Meta:
        ordering = ("id",){% endif %}
