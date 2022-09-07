from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config.config import Config


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.username_input = "username"
        self.password_input = "password"
        self.login_button = "form-button-login"

    def get_username_input(self):
        return self.driver.find_element(By.ID, self.username_input)

    def get_password_input(self):
        return self.driver.find_element(By.ID, self.password_input)

    def get_login_button(self):
        return self.driver.find_element(By.CLASS_NAME, self.login_button)

    def fill_login_data(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, self.username_input))).send_keys(Config.username)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, self.password_input))).send_keys(Config.password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.login_button)))
        self.get_login_button().click()
