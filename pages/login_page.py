from .base_page import BasePage
from .locators import LoginPageLocators
import time
import random

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "It's not Login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRER_FORM), "Registrration form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())

        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.REGISTRER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRER_FORM_PASSWORD_CONFIRMED).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRER_FORM_SUBMIT).click()

