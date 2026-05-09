from .base_page import BasePage
# from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
        f"expected 'login' to be substring of URL, but got: {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(
            By.CSS_SELECTOR, "#login_form"), f"login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(
            By.CSS_SELECTOR, "#register_form"), f"register form is not present"