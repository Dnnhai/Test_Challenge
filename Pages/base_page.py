from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def navigate_to(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def lowercase_string(self, by_string):
        return by_string.lower()

    def remove_space_in_string(self,by_string):
        print('remove space in string "' + by_string+ '---"')
        temp_str = by_string.strip()
        return temp_str

    def press_key(self, by_locator):
    # this function performs press Enter whose locator is passed to it.
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(Keys.ENTER)

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    # this function performs gets text from a web element whose locator is passed to it.
    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return element.text


    def is_visible(self, by_locator):
        print ( "\nCheck the element with the locator" + str(by_locator)+ "is visible or not----")
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return element.is_displayed()
