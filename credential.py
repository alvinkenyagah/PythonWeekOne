class Credential:
    """
    Create blank credential list
    """
    credentials_list=[]
    
    """
    
    """
    def __init__(self, account, loginkey):
        self.account=account
        self.loginkey=loginkey
    """

    """
    def newCredentials(self):
        print("Credential details are "+ self.account+self.loginkey)
    def saveCredential(self):
        Credential.credentials_list.append(self)

    @classmethod
    def findCredential(cls,name):
        for credentials in cls.credentials_list:
            if credentials.account==name:
                return credentials

    def deleteCredential(self):
            Credential.credentials_list.remove(self)

    @classmethod
    def displayCredential(cls):
        return cls.credentials_list