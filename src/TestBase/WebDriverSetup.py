import unittest
import urllib3.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverSetup(unittest.TestCase):

    def setUp(self) -> None:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self) -> None:
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
