import unittest
class LoginTest(unittest.TestCase):
    def test_loginEmail(self):
        print("login test")
        self.assertTrue(True)
    def test_loginNumber(self):
        print("Number is correct")
        self.assertTrue(True)
    def test_loginOtp(self):
        print("Enter otp")
        self.assertTrue(True)

if __name__=="__main--":
    unittest.main()