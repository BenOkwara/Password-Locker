#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(firstname,lastname,email):
    '''
    Function to create a new user
    '''
    new_user = User(firstname,lastname,email)
    return new_user

def create_credential(Email,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(Email,password)
    return new_credential

def save_credential(credential):
    '''
    Function to save the credential
    '''
    credential.save_credential()

def save_users(user):
    '''
    Function to save user
    '''
    user.save_users()

def find_user(email):
    '''
    Function that finds a user by email and returns the user
    '''
    return User.find_by_email(email)

def check_existing_users(first_name):
    '''
    Function that checks if a user exists with the name and returns a Boolean
    '''
    return User.user_exists(first_name)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

'''
<!--------------------------------------------------------- MAIN FUNCTION ---------------------------------------------------------------------->


<!----------------------------------------------------------credentials function --------------------------------------------------------------->
'''
def main():
        print("Hi, Wanna see some Magic? Type your First Name")
        user_name = input()
        print(f"Hello {user_name}. Glad to Visit Password Locker, but, First things First!!")
        print('\n')

        while True:
                print("Use these short codes: cc - create a new credential, ex -exit the credential list ")

                short_code = input().lower()

                if short_code == 'cc':
                        print("-"*15)
                        print("Welcome")
                        print("-"*15)
                        print("Input New Credential")
                        print("-"*15)

                        print ("Emal address ....")
                        email = input()

                        print ("Credetial .....")
                        credential = input()

                        '''
                        Creating and save new credential
                        '''
                        save_credential(create_credential(email,credential))
                        print ('\n')

                        print(f"New Credential {email} {credential} created")
                        print ('\n')
                        print("-"*15)
                else:
                        if short_code == "ex":
                                print("Try Later ......")
                                break
                        else:
                                print("I Didn't Get Your Credentials Well, Repeat")

if __name__ == '__main__':

    main()

'''
<!----------------------------------------------------------user function --------------------------------------------------------------->
'''
def main():
        print("Hi, Wanna see some Magic? Type your First Name")
        user_name = input()
        print(f"Hello {user_name}. Glad to Visit Password Locker")
        print('\n')

        while True:
                print("Use these short codes: cu - create a new user, dis.u -display users, find - find a user, ex -exit the user list ")

                short_code = input().lower()

                if short_code == 'cu':
                        print("-"*15)
                        print("Welcome")
                        print("-"*15)
                        print("New User")
                        print("-"*15)

                        print ("First name ....")
                        firstname = input()

                        print ("Last name .....")
                        lastname = input()

                        print ("Email adress ....")
                        email = input()

                        '''
                        Creating and save new users
                        '''
                        save_users(create_user(firstname,lastname,email))
                        print ('\n')

                        print(f"New User {firstname} {lastname} created")
                        print ('\n')
                        print("-"*15)

                elif short_code == 'dis.u':

                        if display_users():
                                print ("Confirm your credentials")
                                print('\n')

                                for user in display_users():
                                    print(f"{user.first_name} {user.last_name} & {user.email}")

                                print('\n')

                        else:
                                print('\n')
                                print(f"Opps! seems You've Input your credentials wrongly!!")
                                print('\n')

                elif short_code == 'find':

                        print("Enter the detail you want to search for ...")
                        search_detail = input()
                        if check_existing_users(search_detail):
                                search_user = find_user(search_detail)
                                print(f"{search_user.first_name} {search_user.last_name}")
                                print('-' * 15)

                                print (f"Last name ......{search_user.first_name}")
                                print (f"Your Email ......{search_user.email}")

                        else:
                                print("Those credentials don't Exist")

                elif short_code == "ex":
                        print("Try Later ......")
                        break
                else:
                        print("I Didn't Get Your Credentials Well, My Bad!!")


if __name__ == '__main__':

    main()
