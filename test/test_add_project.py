#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_add_project.py
Author  : Dmitry Kruchinin
Date    : 7/7/2021
Desc:   
"""


def test_add_project(app, json_projects):
    project = json_projects
    old_project = app.soap.get_projects_list()
    app.project.create(project)
    new_project = app.soap.get_projects_list()
    old_project.append(project)
    assert len(old_project) == len(new_project)
