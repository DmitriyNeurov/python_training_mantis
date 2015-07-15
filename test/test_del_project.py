from model.project import Project

def test_delete_project(app, db):
    app.session.login("administrator", "root")
    assert app.session.is_logget_in_as("administrator")
    if len(db.get_project_list()) == 0:
        project = Project(name="123")
        app.project.create(project)
    old_projects = db.get_project_list()
    app.project.delete_project()
    app.wd.implicitly_wait(5)
    new_projects = db.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)



