import pyperclip
class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] # Empty user list
    # Init method up here
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)


    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls,number):
        user_found = User.find_by_number(number)
        pyperclip.copy(user_found.number)


    def __init__(self,first_name,last_name,email):

        '''
        __init__ method that defines the properties for my user's object

        Args:
        first_name: New user for first name.
        last_name: New user for last name.
        email: New user for email address.
        '''

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

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
