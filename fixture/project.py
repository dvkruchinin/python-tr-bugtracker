#!/usr/bin/env python
# coding:utf-8
"""
Name    : project.py
Author  : Dmitry Kruchinin
Date    : 7/07/2021
Desc:
"""

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def return_to_manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_elements_by_css_selector("input[value='Create New Project']")

    def fill_forms(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_forms(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        wd.find_elements_by_css_selector("input[value='Create New Project']")
        self.project_cache = None

    def open_manage_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            self.return_to_manage_project_page()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_manage_project_page()
        self.select_project_by_id(id)
        # Submit deletion
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.return_to_manage_project_page()
        self.project_cache = None

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()

    def modification_project_by_id(self, id, new_project_data):
        wd = self.app.wd
        self.open_manage_project_page()
        self.select_project_by_id(id)
        # Open modification form
        wd.find_element_by_name("edit").click()
        self.fill_forms(new_project_data)
        # Submit modification
        wd.find_element_by_name("update").click()
        self.return_to_manage_project_page()
        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.open_manage_project_page()
        return len(wd.find_element_by_css_selector("table tr"))

    def create_project_if_missing(self):
        if self.count() == 0:
            self.create(Project(name="test"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cache = []
            project_table = wd.find_element_by_class_name("form-container")
            for row in project_table.find_elements_by_tag_name("table tbody tr"):
                cells = row.find_elements_by_tag_name("td")
                project_name = cells[0].text
                id = cells[0].find_element_by_tag_name("a").get_attribute("href").split("=")[1]
                self.project_cache.append(Project(name=project_name, id=id))
        return list(self.project_cache)
