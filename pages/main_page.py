from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def go_to_login_page(self):
        # login_link = WebDriverWait(self.browser, 30).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#login_link")))
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(
            By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
