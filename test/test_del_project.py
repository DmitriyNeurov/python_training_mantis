from model.project import Project
import random

def test_delete_project(app):
    if app.get_project_list() == 0:
        app.project.create(Project(name="Dmitriy"))
    old_projects = app.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project()
    app.wd.implicitly_wait(5)
    new_projects = app.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects
