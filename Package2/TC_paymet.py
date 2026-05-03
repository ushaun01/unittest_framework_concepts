import unittest
class Payment(unittest.TestCase):

    def test_rubel(self):
        print("Payment in Rubel")
        self.assertTrue(True)

    def test_rupees(self):
        print("Payment in rupees")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()