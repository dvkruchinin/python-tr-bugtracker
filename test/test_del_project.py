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
    app.project.open_manage_project_page()
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_project = app.project.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    new_project = app.project.get_project_list()
    old_project.remove(project)
    assert len(old_project) == len(new_project)

