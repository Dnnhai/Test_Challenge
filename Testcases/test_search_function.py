from Testcases.base_test import BaseTest
from Pages.main_page import MainPage
from Pages.article_page import ArticlePage
from Testdata.test_data import Data
from Pages.login_page import LoginPage
from Pages.base_page import BasePage
import unittest
text_in_search = "Ho Chi Minh"
main_title = "Wikipedia, the free encyclopedia"
class TestSearchFunction(BaseTest):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
    ##TC-0002 Verify search function can work in case user not login with exact keyword
    def test_search_result_incase_user_not_login_with_exact_keyword(self):
        print("\n Verify Keyword in search box disappears after search result displayed----")

        search_act = MainPage(self.driver)
        first_heading = ArticlePage(self.driver)
        search_act.input_text_to_search_box(text_in_search)
        search_act.click_search_button()

        #get fisrt heading of search result
        heading_text = first_heading.get_first_heading()
        heading_text = first_heading.lowercase_string(heading_text)
        heading_text = first_heading.remove_space_in_string(heading_text)

        search_text = first_heading.lowercase_string(text_in_search)
        search_text = first_heading.remove_space_in_string(search_text)

        #compare search string with search result
        assert (search_text==heading_text)

    @unittest.skip
    ##TC-0003 Verify search function can work with exact keyword when user login with valid account
    def test_search_result_incase_user_login_with_exact_keyword(self):
        print("\n Verify search function can work with exact keyword when user login with valid account----")

        username = Data.USERNAME
        password = Data.PASSWORD

        main_page = MainPage(self.driver)
        main_page.click_log_in_accesskey()

        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        main_page_title = BasePage(self.driver).get_title()
        # check the login result
        assert main_page_title == main_title, "test passed"

        search_act = MainPage(self.driver)
        first_heading = ArticlePage(self.driver)
        search_act.input_text_to_search_box(text_in_search)
        search_act.click_search_button()

        #get fisrt heading of search result
        heading_text = first_heading.get_first_heading()
        heading_text = first_heading.lowercase_string(heading_text)
        heading_text = first_heading.remove_space_in_string(heading_text)

        search_text = first_heading.lowercase_string(text_in_search)
        search_text = first_heading.remove_space_in_string(search_text)

        #compare search string with search result
        assert (search_text==heading_text)

