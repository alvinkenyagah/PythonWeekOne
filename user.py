from cryptography.fernet import Fernet

class Person:
     person_list=[]
     def __init__(self,username, password):          
          self.username = username
          self.password = password
     def newUser(self):
          print("User details are "+ self.username+self.password)
     def saveUser(self):
          Person.person_list.append(self)



# """Generate new key
# """
# key = Fernet.generate_key()
# print(key)

# """Convert entered string to bits
# """

# password = raw_input("ENTER PASSWORD: ").encode

# f_obj = Fernet(key)
# encrypted_password = f_obj.encrypted(password)
# new_object = Person(social, username, password)

# decrypt_password = f_obj.decrypt(password)
# print(decrypted_password)
