import time
import unittest
import HtmlTestRunner

from Testcases.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.special_page import SpecialPage
from Testdata.test_data import Data
from Pages.base_page import BasePage

main_title = "Wikipedia, the free encyclopedia"
log_out_title = "Log out"
message_error = "Incorrect username or password entered. Please try again."

class TestLoginPage1(BaseTest):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    ##TC-0004: Verify user can login with valid account and after that logout
    def test_loign_with_valid_acc_and_logout(self):
        print("\nVerify user can login with valid account and after that logout----")
        username = Data.USERNAME
        password = Data.PASSWORD

        main_page = MainPage(self.driver)
        main_page.click_log_in_accesskey()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        main_page_title = BasePage(self.driver).get_title()
        #check the login result
        assert main_page_title == main_title, "test passed"

        main_page.click_log_out_accesskey()
        heading = SpecialPage(self.driver).get_heading()
        #check the logout result
        assert heading ==log_out_title, "test passed"


    ## TC-0005:Verify user can not login with invalid account
    def test_loign_with_invalid_acc(self):
        print("\n\n Verify user can not login with invalid account----")

        username = Data.WRONG_USERNAME
        password = Data.PASSWORD

        main_page = MainPage(self.driver)
        main_page.click_log_in_accesskey()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        message_err = login_page.get_error_mesasage()
        #check the login result in case fail
        assert message_err == message_error+"a", "test passed"

if __name__ == '__main__':
    unittest.main()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))