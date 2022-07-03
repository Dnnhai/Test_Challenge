from Pages.base_page import BasePage
from Locators.main_page_locators import MainPageLocators
from Testdata.test_data import Data

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        print("\nNavigate to base url----")
        self.navigate_to(Data.BASE_URL)

    def click_log_in_accesskey(self):
        print("\nClick on accesskey 'Log in' ----")
        self.click(MainPageLocators.LOGIN_ACCESSKEY)

    def click_log_out_accesskey(self):
        print("\nClick on accesskey 'Log out'----")
        self.click(MainPageLocators.LOGOUT_ACCESSKEY)

    def click_talk_accesskey(self):
        print("\nClick on accesskey 'Talk' ----")
        self.click(MainPageLocators.TALK_ACCESSKEY)

    def input_text_to_search_box(self, text):
        print("\nInput text to search box----")
        self.enter_text(MainPageLocators.SEARCH_BOX, text)

    def press_enter(self):
        print("\nPress Enter at search box----")
        self.press_key(MainPageLocators.SEARCH_BOX)

    def click_search_button(self):
        print("\nclick search button----")
        self.click(MainPageLocators.SEARCH_BUTTON)
