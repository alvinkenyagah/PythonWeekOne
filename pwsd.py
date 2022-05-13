# from cryptography.fernet import Fernet
from cryptography.fernet import Fernet

"""
Function that generate new key
"""
key = Fernet.generate_key()

"""
Convert strings to bytes
"""
pswd = input("Enter your password : ").encode()

f_obj = Fernet(key)

encrypt_pswd = f_obj.encrypt(pswd)

print(encrypt_pswd)

decrypted_pswd = f_obj.decrypt(pswd)
print(decrypted_pswd)
