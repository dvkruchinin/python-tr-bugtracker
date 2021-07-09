#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_del_project.py
Author  : Dmitry Kruchinin
Date    : 7/7/2021
Desc:   
"""

import random
from model.project import Project


def test_del_project(app):
    if len(app.soap.get_projects_list()) == 0:
        app.project.create(Project(name="test"))
    old_project = app.soap.get_projects_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project)
    new_project = app.soap.get_projects_list()
    old_project.remove(project)
    assert len(old_project) == len(new_project)

