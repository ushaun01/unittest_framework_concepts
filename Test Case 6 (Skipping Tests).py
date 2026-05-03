#skip test
#skip test with reason
#skip test with based on condition

import unittest
class AppTesting(unittest.TestCase):

    @unittest.SkipTest                                 #by skip test
    def test_search(self):
        print("Search Test")

    @unittest.skip("Still it is  not ready")           #skip test with reason
    def test_advanced(self):
        print("Advanced Search")

    @unittest.skipIf(1==1,"One  is equal to one")    #if condition is true, this method is skipped
    def test_modern(self):
        print("Modern Search")

    def test_login(self):
        print("Logged in gmail")

    def test_logout(self):
        print("Logged Out From gmail")

if __name__=="__main__":
    unittest.main()