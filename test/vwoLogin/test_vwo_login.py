import time

import allure
import pytest
from selenium import webdriver
from test.pageObject.loginPage import LoginPage
from test.pageObject.dashboardPage import Dashboard

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    return driver

@allure.epic("VWO Login Test")
@allure.feature("TC0 - VWO app Negative test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    login = LoginPage(driver)
    login.login_to_vwo(usr="py2x@thetestingacademy.com", pwd="Wingi234")
    time.sleep(5)
    error_message = login.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"
    # assert "Your email, password, IP address or location did not match" in login.get_error_message_text()

@allure.epic("VWO Login Test")
@allure.feature("TC1 - VWO app Positive test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    login = LoginPage(driver)
    login.login_to_vwo(usr="py2x@thetestingacademy.com", pwd="Wingify@1234")
    time.sleep(10)
    dashboard = Dashboard(driver)
    dashboard.get_logged_in_user()
    assert "Dashboard" in driver.title
    print(driver.title)
    assert "Aman" in dashboard.user_logged_in_text()
