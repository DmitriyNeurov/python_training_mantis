from model.project import Project
import string
import random

def random_project(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_project(app):
    old_projects = app.soap.get_project_list("administrator", "root")
    app.session.login("administrator", "root")
    assert app.session.is_logget_in_as("administrator")
    project = Project(name=(random_project("prj_", 10)))
    app.project.create(project.name)
    app.wd.implicitly_wait(5)
    new_projects = app.soap.get_project_list("administrator", "root")
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
