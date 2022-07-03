from Locators.sub_page_locators import SubPageLocators
from Pages.base_page import BasePage

class SubPage(BasePage):

    def get_subpage_heading(self):
        print("\nget sub page first heading----")
        return self.get_text(SubPageLocators.SUBPAGE_FIRST_HEADING)

