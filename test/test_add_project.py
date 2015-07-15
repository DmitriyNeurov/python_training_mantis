from model.project import Project

def test_add_project(app, db):
    old_projects = db.get_project_list()
    app.session.login("administrator", "root")
    assert app.session.is_logget_in_as("administrator")
    project = Project(name="123")
    app.project.create(project)
    app.wd.implicitly_wait(5)
    new_projects = db.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
