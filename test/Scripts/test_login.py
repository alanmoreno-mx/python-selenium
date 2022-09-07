import time
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage
from src.PageObject.Pages.LoginPage import LoginPage
from config.config import Config


class Test_Login(WebDriverSetup):

    def testLogin(self):
        driver = self.driver
        self.driver.get(Config.base_url)
        home_page = HomePage(driver)
        time.sleep(2)
        home_page.click_home_user_button()
        login_page = LoginPage(driver)
        login_page.fill_login_data()
        login_page.click_login_button()
