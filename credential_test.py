import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines the test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

def setUp(self):
    '''
    Set up method to run before each test casesself.
    '''
    self.new_credential = Credential("bensonwaweru47@gmail.com", "Jesusiscoming") # creating user object

def test_init(self):
    '''
    test_init test cases to test if the object is initialized properly
    '''

    self.assertEqual(self.new_credential.email,"bensonwaweru47@gmail.com")
    self.assertEqual(self.new_credential.Password,"Jesusiscoming")

def test_save_credential(self):
    '''
    test_save_credential test case to test if the credential object is saved into the credential_list
    '''
    self.new_credential.save_credential() # saving the new user
    self.assertEqual(len(Credential.credential_list),1)

def tearDown(self):
    '''
    tearDown method it cleans up after each test case has run.
    '''
    Credential.credential_list = []

def test_save_multiple_credential(self):
    '''
    test_save_multiple_credential to check if the credential can be able to save multiple user objects to our credential_list
    '''
    self.new_credential.save_credential()
    test_credential = Credential("Test","credential","test@credential.com") # new users
    test_credential.save_credential()
    self.assertEqual(len(Credential.credential_list),2)



if __name__ =='__main__':
    unittest.main()
