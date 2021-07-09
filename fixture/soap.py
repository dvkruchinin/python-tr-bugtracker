#!/usr/bin/env python
# coding:utf-8
"""
Name    : soap.py
Author  : Dmitry Kruchinin
Date    : 7/9/2021
Desc:   
"""

from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client("http://localhost/mantisbt-1.3.20/api/soap/mantisconnect.php?wsdl")

    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        result = self.client.service.mc_projects_get_user_accessible(
            self.app.config['webadmin']['username'], self.app.config['webadmin']['password'])
        projects = list(map(lambda x: x.id, result))
        return projects
