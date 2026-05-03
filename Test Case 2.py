import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    def test_chrome(self):                                                              #test name always start with test
        self.driver=webdriver.Chrome()                                                   #self is written as belongs to particular fun
        self.driver.get("https://www.facebook.com/")
        print(self.driver.title)
        self.driver.close()

    def test_google(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        self.driver.close()

if __name__=="__main__":
    unittest.main()