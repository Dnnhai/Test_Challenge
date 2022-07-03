from Locators.atricle_page_locators import ArticlePageLocator
from Pages.base_page import BasePage

class ArticlePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_heading(self):
        return self.get_text(ArticlePageLocator.FRIST_HEADING)
