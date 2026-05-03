#Relational Comparison
#assetGreater
#assertGreaterEqual
#assertLess
#assertLessEqual

import unittest
class Test(unittest.TestCase):
    def testName(self):

        #assertGreater
        self.assertGreater(100,10)             #passed as first value is greater

        # assertGreaterEqual
        self.assertGreaterEqual(10, 20, "A is smaller than b")  # failed as 'a' is small and it through msg

        # assertLess
        self.assertLess(100,30)              #failed as 'a' is not less than b

        # assertLessEqual
        self.assertLessEqual(5,25,"a is less than b")     #passed as 'a' is less


if __name__=="__main__":
    unittest.main()