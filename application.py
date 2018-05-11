from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def return_group_page(self):
            wd = self.wd
            # return to group page
            wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self):
            wd = self.wd
            # submit group creation
            wd.find_element_by_name("submit").click()
            self.return_group_page()

    def fill_group_firm(self, name, footer, headers):
            wd = self.wd
            # fill group firm
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(name)
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(headers)
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(footer)

    def init_group_creation(self):
            wd = self.wd
            # init group creation
            self.Open_home_page()
            self.open_group_page()
            wd.find_element_by_name("new").click()

    def open_group_page(self):
            wd = self.wd
            # open_group_page
            wd.find_element_by_link_text("groups").click()

    def Open_home_page(self):
            wd = self.wd
            # open home page
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()