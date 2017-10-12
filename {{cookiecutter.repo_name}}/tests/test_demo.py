# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import pytest
from demo.models import DemoModel


@pytest.mark.django_db(transaction=False)
def test_model():
    m = DemoModel()
    m.save()
    assert m.pk
