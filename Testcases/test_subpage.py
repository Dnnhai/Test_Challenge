import unittest

from Testcases.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.sub_page import SubPage
from Testdata.test_data import Data
from Pages.base_page import BasePage

text_in_search = "Ho Chi Minh"
main_title = "Wikipedia, the free encyclopedia"
subpage_first_heading = "User talk:"+Data.USERNAME
class TestSubpage(BaseTest):

    ##TC-0008: Verify heading of Talk subpage include username when user loggin with valid account
    def test_sub_page_heading(self):
        print("\n Verify heading of Talk subpage include username when user loggin with valid account----")
        username = Data.USERNAME
        password = Data.PASSWORD

        main_page = MainPage(self.driver)
        main_page.click_log_in_accesskey()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        main_page.click_talk_accesskey()

        subpage = SubPage(self.driver)
        sub_heading = subpage.get_subpage_heading()
        #check the subpage_first_heading  has form: " User talk:<username>"
        assert (subpage_first_heading==sub_heading)

if __name__ == '__main__':
    unittest.main()