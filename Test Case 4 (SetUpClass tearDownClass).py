import unittest


class AppTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is login")
    def test_search(self):
        print("Search")

    def test_advance(self):
        print("Advance")

    def test_prepaid(self):
        print("prepaid")

    @classmethod
    def tearDownClass(cls):
        print("This is Logout")

if __name__ == "__main__":
    unittest.main()
