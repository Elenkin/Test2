from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper

class Application:

    def __init__(self):
            self.wd = WebDriver()
            self.wd.implicitly_wait(60)
            self.group = GroupHelper(self)

    def destroy(self):
            self.wd.quit()