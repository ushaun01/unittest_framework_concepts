import unittest
from Package1.TC_login import LoginTest
from Package1.TC_signup import SignUpTest

from Package2.TC_paymet import Payment
from Package2.TC_return import PaymentReturn

#get all test
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(Payment)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)

#create test suites
sanityTestSuite=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(sanityTestSuite)

functionTestSuite=unittest.TestSuite([tc3,tc4])
unittest.TextTestRunner().run(functionTestSuite)

masterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)                 #verbosity give al info