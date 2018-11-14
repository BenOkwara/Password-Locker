import pyperclip
class User:
    '''
    Class that generates new instances of users
    '''

    # Init method up here
    def __init__(self,first_name,last_name,email):

        '''
        __init__ method that defines the properties for my user's object

        Args:
        first_name: New user for first name.
        last_name: New user for last name.
        email: New user for email address.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.email = email


    user_list = [] # Empty user list

    def save_users(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)


    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
            email: email to search for
        Returns :
            User of person that matches the email.
        '''

        for user in cls.user_list:
            if user.email == email:
                return user

    @classmethod
    def user_exists(cls,first_name):
        '''
        This Method checks if a user exist from the user list

        Args:
            first_name: first_name to search if it user_exists
        Returns:
            Boolean: True or False depending if the user exists
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        This method returns the user list
        '''
        return cls.user_list
