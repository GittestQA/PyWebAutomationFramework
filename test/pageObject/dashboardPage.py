
from selenium.webdriver.common.by import By

class Dashboard:

    def __init__(self, driver):
        self.driver = driver

# Page class
# Page locators
# Page actions

    user_logged_in = (By.XPATH,"//span[@class='Fw(semi-bold) ng-binding']")

    def get_logged_in_user(self):
        return self.driver.find_element(*Dashboard.user_logged_in)

    def user_logged_in_text(self):
        return self.get_logged_in_user().text