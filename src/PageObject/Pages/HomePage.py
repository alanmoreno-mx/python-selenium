from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.home_user_button = "//a[text()='Dexcom Clarity for Home Users']"

    def get_home_user_button(self):
        return self.driver.find_element(By.XPATH, self.home_user_button)

    def click_home_user_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.home_user_button))).click()


