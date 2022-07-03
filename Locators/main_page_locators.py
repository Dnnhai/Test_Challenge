from selenium.webdriver.common.by import By


class MainPageLocators:


    LOGIN_ACCESSKEY = (By.XPATH, '//a[@accesskey="o"]')
    TALK_ACCESSKEY = (By.XPATH, '//a[@accesskey="n"]')
    PERSON_NOT_LOGIN = (By.XPATH, '//span[text()="Not logged in"]')
    LOGOUT_ACCESSKEY = (By.XPATH, '//span[text()="Log out"]')

    SEARCH_BOX = (By.XPATH, '//input[@class="vector-search-box-input"]')
    SEARCH_BUTTON = (By.XPATH, '//input[@id="searchButton"]')
    BELL_ICON = (By.XPATH,'//a[@title="Your alerts"]')