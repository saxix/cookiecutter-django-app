# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from factory import DjangoModelFactory


class DemoModelFactory(DjangoModelFactory):
    class Meta:
        model = 'demo.DemoModel'
        django_get_or_create = ('id',)
