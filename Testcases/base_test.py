
import sys
import unittest
from selenium import webdriver
sys.path.append(".")


# Base class for the test
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
        self.driver.maximize_window()

    def tearDown(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            pass


