# import logging
from Locators.login_page_locators import LoginPageLocators
from Pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_error_mesasage(self):
        return self.get_text(LoginPageLocators.MESSAGE_ERROR)


    def login(self, username, password):
        print("\nInput valid username and password----")
        self.enter_text(LoginPageLocators.USERNAME, username)
        self.enter_text(LoginPageLocators.PASSWORD, password)
        print("\nClick on button 'Log in'")
        self.click(LoginPageLocators.BUTTON_LOGIN)

