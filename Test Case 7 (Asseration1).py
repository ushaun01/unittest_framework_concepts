#assertEqual
#assertNotEqual

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")
        a=driver.title

        #assertEqual
        #self.assertEqual("Google",a,"web page title is not same")            #msg=error message if not matched


        #assertNotEqual           #it is passed if it not-matched
        self.assertNotEqual("Google123",a)



if __name__=="__main__":
    unittest.main()