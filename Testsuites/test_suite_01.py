# import sys
# sys.path.append(".")
from HtmlTestRunner import *
from unittest import *
from Testcases.test_login_page import TestLoginPage1
from Testcases.test_subpage import TestSubpage
from Testcases.test_search_function import TestSearchFunction
from Testcases.test_menu_content_list import TestMenuContentList

# get all tests from Login class
#
# login1 = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage1)
#
# # create a test suite
# test_suite = unittest.TestSuite([login1])
#
# # run the suite
# unittest.TextTestRunner(verbosity=2).run(test_suite)

test_login = TestLoader().loadTestsFromTestCase(TestLoginPage1)
test_subpage = TestLoader().loadTestsFromTestCase(TestSubpage)
test_search = TestLoader().loadTestsFromTestCase(TestSearchFunction)
test_menu = TestLoader().loadTestsFromTestCase(TestMenuContentList)


suite = TestSuite([test_login, test_subpage,test_search,test_menu])

runner = HTMLTestRunner(output='Reports', combine_reports=True,report_name="testSuiteReport_01", add_timestamp=True)
runner.run(suite)






