from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_Manage_Projects(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

  #  def change_field_value(self, field_name, text):
  #      wd = self.app.wd
   #     if text is not None:
   #         wd.find_element_by_name(field_name).click()
   #         wd.find_element_by_name(field_name).clear()
    #        wd.find_element_by_name(field_name).send_keys(text)

   # def fill_project_form(self, project):
   #     wd = self.app.wd
    #    self.change_field_value("project_name", project.name)

    def create(self, project):
        wd = self.app.wd
        self.open_Manage_Projects()
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("qwert")
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("gfhhgfhhf")
        wd.find_element_by_css_selector("input.button").click()
        # submit contact creation
        wd.find_element_by_link_text("Add Project").click()
        self.project_cash = None

  #  def select_first_project(self):
  #     wd = self.app.wd
  #      wd.find_element_by_name("selected[]").click()

    #def select_project_by_id(self, id):
      #  wd = self.app.wd
       # wd.find_element_by_css_selector("input[value='%s']" %id).click()

    def delete_project(self):
        wd = self.app.wd
        self.open_Manage_Projects()
        wd.find_element_by_link_text("qwert").click()
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_css_selector("input.button").click()
        self.project_cash = None
   # def delete_project_by_index(self, index):
      #  wd = self.app.wd
      #  self.app.open_home_page()
      #  self.select_project_by_index(index)
      #  wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
      #  wd.switch_to_alert().accept()
      #  self.contact_cash = None

   # def delete_project_by_id(self, id):
    #    wd = self.app.wd
    #    self.app.open_home_page()
    #    self.select_project_by_id(id)
    #    wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
    #    wd.switch_to_alert().accept()
    #    self.contact_cash = None


   # def count(self):
    #    wd = self.app.wd
     #   self.app.open_home_page()
    #    return len(wd.find_elements_by_name("selected[]"))

    contact_cash=None

    def get_project_list(self):
        if self.project_cash is None:
            wd = self.app.wd
            self.open_Manage_Projects()
            self.project_cash = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                self.project_cash.append(Project(name=name))

        return list(self.project_cash)











