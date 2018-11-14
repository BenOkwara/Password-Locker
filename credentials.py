class credentials:
    '''
    Class that generates new instances of credentials
    '''

    def __init__(self,email,Password):
        '''
        __init__ method that defines the properties the credentials object

        Args:
        email: New credentials for email address.
        Password: New credentials for Password
        '''

        self.email = email
        self.Password = Password

    credentials_list = [] # Empty credentials list
