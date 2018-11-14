#!/usr/bin/env python3.6
from user import User

def create_user(firstname,lastname,email):
    '''
    Function to create a new user
    '''
    new_user = User(firstname,lastname,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_users()
