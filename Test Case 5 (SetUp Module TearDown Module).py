import unittest
def setUpModule():
    print("Setup")

def tearDownModule():
    print("teardown module")

class AppTesting(unittest.TestCase):

    def test_search(self):
        print("Search")

    def test_advance(self):
        print("Advance")

    def test_prepaid(self):
        print("prepaid")

if __name__ == "__main__":
    unittest.main()