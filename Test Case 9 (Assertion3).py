#assertIsNone
#assertIsNotNone

import unittest
from selenium import webdriver

#assert is none
class Test(unittest.TestCase):
    def testName(self):
        driver=None
        self.assertIsNone(driver)



#assert is not none
class Test1(unittest.TestCase):
    def testName1(self):
        driver=webdriver.Chrome()
        self.assertIsNotNone(driver)


if __name__=="__main__":
    unittest.main()