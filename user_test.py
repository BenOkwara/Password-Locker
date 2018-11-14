import unittest # Importing unittest module
from user import User # Importing the user class
import pyperclip

class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for the user class behavioursself.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test casesself.
        '''
        self.new_user = User("Jimmy","Benson","bensonwaweru47@gmail.com") # creating user object

    def test_init(self):
        '''
        test_init test cases to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Jimmy")
        self.assertEqual(self.new_user.last_name,"Benson")
        self.assertEqual(self.new_user.email,"bensonwaweru47@gmail.com")

    def tearDown(self):
        '''
        tearDown method it cleans up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if the user can be able to save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","test@user.com") # new users
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user_list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_email(self):
        '''
        Test to check if we can find a user by email and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","bensonwaweru47@gmail.com") # new user
        test_user.save_user()

        found_user = User.find_by_email("bensonwaweru47@gmail.com")

        self.assertEqual(found_user.email,test_user.email)

    def test_user_exists(self):
        '''
        Test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","test@user.com") # new user
        test_user.save_user()

        user_exists = User.user_exists("Jimmy")

        self.assertTrue(user_exists)

    # def test_display_all_users(self):
    #     '''
    #     method that returns a list of all users saved
    #     '''
    #     self.assertEqual(User.display_users(),User.user_list)
    #
    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we can copy an email address from a found test_display_all_users
    #     '''
    #     self.new_user.save_user()
    #     User.copy_email("bensonwaweru47@gmail.com")
    #
    #     self.assertEqual(self.new_user.email,pyperclip.paste())

    # def test_user_exists(self):
    #     '''
    #     test to check if i can return a boolean if the we don't find any existing users
    #     '''
    #     self.new_user.save_user()
    #     test_user = User("Test","user","test@user.com") # new
    #     test_user.save_user()
    #
    #     user_exists = User.user_exists("Benson")
    #
    #     self.assertEqual(user_exists)
    #
    # @classmethod
    # def user_exists(cls,last_number):
    #
    #     '''
    #     This is a method that checks whether user exist at the user_list
    #     Args:
    #         Last name to check if the user really exist.
    #     Boolean: Trie or false depending if the user exist
    #     '''
    #
    #     for user in cls.user_list:
    #         if user.last_name == last_name:
    #                 return True
    #
    #     return False
























if __name__ =='__main__':
    unittest.main()
