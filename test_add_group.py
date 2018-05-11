# -*- coding: utf-8 -*-

import pytest
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        success = True
        app.init_group_creation()
        app.fill_group_firm(name="Новая группа777", footer="неуненен", headers="содержание")
        app.submit_group_creation()

def test_add_empty_group(app):
        success = True
        app.init_group_creation()
        app.fill_group_firm(name="", footer="", headers="")
        app.submit_group_creation()


