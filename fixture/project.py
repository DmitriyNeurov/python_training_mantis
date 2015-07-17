
class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_Manage_Projects(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.19/manage_proj_page.php")

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, project):
        wd = self.app.wd
        self.open_Manage_Projects()
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()
        self.change_field_value("name", project)
        wd.find_element_by_css_selector("input.button").click()
        self.project_cash = None

    def delete_project(self, project):
        wd = self.app.wd
        self.open_Manage_Projects()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_css_selector("input.button").click()
        self.project_cash = None

