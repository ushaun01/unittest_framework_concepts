#assertTrue
#assertFalse

import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")
        a=driver.title

        #assertTrue
        self.assertTrue(a=="Google")

        #assertFalse
        self.assertFalse(a=="Google12")         #it is passed as it is matched

if __name__=="__main__":
    unittest.main()