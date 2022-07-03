import time

from Testcases.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Testdata.test_data import Data
from Pages.base_page import BasePage
from Locators.main_page_locators import MainPageLocators

class TestMenuContentList(BaseTest):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    #TC-0006: Verify Menu content list include "Bell icon" when valid account loged in
    def test_menu_content_list_has_bell_icon(self):
        username = Data.USERNAME
        password = Data.PASSWORD

        main_page = MainPage(self.driver)
        main_page.click_log_in_accesskey()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        content_list = BasePage(self.driver)
        #check bell icon is visible or not
        bell_icon = content_list.is_visible(MainPageLocators.BELL_ICON)
        assert(bell_icon==True), "test passed"

        if(bell_icon == True): print("\nBell icon is visible")
        else:print("\nBell icon is invisible")

    ##TC-0007: Verify Menu content list include "Not Logged in" when user not loged in
    def test_menu_content_list_has_person_icon_with_Not_LoggedIn_string(self):

        content_list = MainPage(self.driver)
        #check Person icon wiht text Not logged in
        print("\nCheck person icon content string: 'Not Logged in'----")
        person_icon = content_list.get_text(MainPageLocators.PERSON_NOT_LOGIN)
        assert person_icon == "Not logged in", "test passed"