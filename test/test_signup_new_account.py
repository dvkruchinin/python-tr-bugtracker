#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_signup_new_account.py
Author  : Dmitry Kruchinin
Date    : 7/7/2021
Desc:   
"""

import random
import string


def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_signup_new_account(app):
    app.session.ensure_logout()
    username = random_username("user_", 10)
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exist(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)
