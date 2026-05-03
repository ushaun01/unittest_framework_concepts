#assertIN
#assertNotIn

import unittest

class Test(unittest.TestCase):
    def testName(self):
        list=["python","selenium","sql","java"]
        #assertIn
        self.assertIn("python",list)                    #passed
        self.assertIn("ruby",list)                      #failed as ruby is not part
        #assetNotIn
        self.assertNotIn("Sql",list)                    #passed as Sql is not in list

if __name__=="__main__":
    unittest.main()
