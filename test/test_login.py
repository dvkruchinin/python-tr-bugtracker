#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_login.py
Author  : Dmitry Kruchinin
Date    : 7/7/2021
Desc:   
"""


def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
