# import logging
from Locators.special_page_locators import SpecialPageLocators
from Pages.base_page import BasePage

class SpecialPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_heading(self):
        # special_page = BasePage(self.driver)
        # heading = special_page.get_text(SpecialPageLocators.LOG_OUT_HEADING)
        print("\nGet heading form special page----")
        return self.get_text(SpecialPageLocators.LOG_OUT_HEADING)




