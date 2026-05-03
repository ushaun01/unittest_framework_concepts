import unittest

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is login")

    @classmethod
    def tearDown(self):
        print("This is Logout")

    def test_search(self):
        print("Search")

    def test_advance(self):
        print("advance")

    def test_prepaid(self):
        print("prepaid")

if __name__=="__main__":
    unittest.main()
