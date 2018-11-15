class Credential:
    '''
    Class that generates new instances of credential
    '''

    def __init__(self,email,Password):
        '''
        __init__ method that defines the properties the credential object

        Args:
        email: New credential for email address.
        Password: New credential for Password
        '''

        self.email = email
        self.Password = Password

    credential_list = [] # Empty credentials list
    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''
        Credential.credential_list.append(self)
