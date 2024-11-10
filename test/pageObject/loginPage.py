# Page class
#
# Page Locators
# Page Actions
# Web driver init
# Custom functions
# No assertions in Page object

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

# Page Locators

    username = (By.ID, "login-username")
    password = (By.XPATH, "//input[@id='login-password']")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    error_message = (By.XPATH, "//div[@id='js-notification-box-msg']")
    # forgot_password_button =()
    # free_trial = ()
    # remember_checkbox = (By.XPATH, "")
    # sso_login = ()

# Page Actions

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)
    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)
    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

# Page Action - Main Action

    def login_to_vwo(self, usr, pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

