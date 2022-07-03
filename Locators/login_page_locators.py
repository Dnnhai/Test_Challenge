from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.XPATH, '//input[@name="wpName"]')
    PASSWORD = (By.XPATH, '//input[@name="wpPassword"]')
    BUTTON_LOGIN = (By.XPATH, '//button[@name="wploginattempt"]')
    MESSAGE_ERROR = (By.XPATH, '//div[@class="mw-message-box-error mw-message-box"]')