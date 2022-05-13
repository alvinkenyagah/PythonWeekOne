import random
import random, string
from user import Person
from credential import Credential


def create_user(username, password):
    new_user=Person(username, password)
    return new_user

def create_credentials(account, loginkey):
    new_credentials=Credential(account, loginkey)
    return new_credentials

def generate_loginkey():
    password=password=string.digits+string.ascii_letters
    while True:
        try:
            length=int(input("Enter length of login key "))
            signinkey=random.sample(password, length)
        except ValueError:
            print("Please check your input")
            continue
        else:
            loginkey=("".join(signinkey))
def saveCredential(credential):
    credential.saveCredential()
def deleteCredential(credential):
    credential.deleteCredential()
def displayCredentials():
    return Credential.displayCredential()
def findCredential(accountname):
    return Credential.findCredential(accountname)



def main():
    print("Hello Welcome to your contact list. What is your name?")

    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("lg=>Login to your account")
        print("ca=>Create new account")
        short_code = input().lower()
        print('\n')
        if short_code =='lg':
            print("Enter user name ")
            user_name= input()
            print("Enter password ")
            password= input()
            while user_name != user_name1 or password != password1:
                print("Wrong user name or password")
            else:
                print("Login successful")
                while True:
                    print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, dl - delete credential, ex -exit the application ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New account")
                            name= input()
                            while True:
                                print("Use these short codes : nk - generate new key, ok - enter own key ")
                                key= input().lower()
                            
                                if key== 'ok':
                                    print("Enter password ")
                                    pwsd= input()
                                    break
                                elif key== 'nk':
                                    pwsd=generate_loginkey()
                                    break                                 
                                else:
                                    print("Enter the required shortcodes")
                            saveCredential(create_credentials(name, pwsd))
                            print(f"Credentials for {name} have been created")
                    elif short_code == 'dc':
                        if displayCredentials():
                            print("Find your saved credentials here ")
                            for credentials in displayCredentials():
                                print(f"{credentials.account}-{credentials.loginkey}")
                        else:
                            print("You do not have any saved credentials")
                    elif short_code == 'dl':
                        print("Enter the name of the account you wish to delete")
                        accountname=input()
                        account=findCredential(accountname)
                        deleteCredential(account)
                    elif short_code == 'fc':
                        print("Enter the name of the account")
                        accountcred=input()
                        acc=findCredential(accountcred)
                        print(f"{acc}")
                    else:
                        print("Enter a valid short code to continue")
        elif short_code == 'ca':
            print("Enter a user name")
            user_name1=input()
            print("Enter password")
            password1=input()
            print("Confirm password")
            confirm=input()
            while confirm != password1:
                print("Passwords do not match")
                print("Enter password")
                password1=input()
                print("Confirm password")
                confirm=input()
            else:
                print("Your account was created successfully")
                print("Proceed to login")
                print("Enter user name")
                user_name=input()
                print("Enter your password")
                password=input()
                while user_name != user_name1 or password != password1:
                    print("Invalid username or password")
                    print("Enter user name")
                    user_name=input()
                    print("Enter your password")
                    password=input()
                else:
                    print(f"Welcome to your account{user_name}")
                    while True:
                        print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, dl - delete credential, ex -exit the application ")

                        short_code = input().lower()

                        if short_code == 'cc':
                                print("New account")
                                name= input()
                                while True:
                                    print("Use these short codes : nk - generate new key, ok - enter own key ")
                                    key= input().lower()
                                
                                    if key== 'ok':
                                        print("Enter password ")
                                        pwsd= input()
                                    elif key== 'nk':
                                        pwsd=generate_loginkey()
                                        break
                                    else:
                                        print("Enter the required shortcodes")
                                saveCredential(create_credentials(name, pwsd))
                                print(f"Credentials for {name} have been created")
                        elif short_code == 'dc':
                            if displayCredentials():
                                print("Find your saved credentials here ")
                                for credentials in displayCredentials():
                                    print(f"{credentials.account}-{credentials.loginkey}")
                            else:
                                print("You do not have any saved credentials")
                        elif short_code == 'dl':
                            print("Enter the name of the account you wish to delete")
                            accountname=input()
                            account=findCredential(accountname)
                            deleteCredential(account)
                        elif short_code == 'fc':
                            print("Enter the name of the account")
                            accountcred=input()
                            acc=findCredential(accountcred)
                            print(f"{acc}")
                        else:
                            print("Enter a valid short code to continue")









                        #     print("First name ....")
                        #     f_name = input()

                        #     print("Last name ...")
                        #     l_name = input()

                        #     print("Phone number ...")
                        #     p_number = input()

                        #     print("Email address ...")
                        #     e_address = input()

                        #     # create and save new contact.
                        #     save_contacts(create_contact(
                        #         f_name, l_name, p_number, e_address))
                        #     print('\n')
                        #     print(f"New Contact {f_name} {l_name} created")
                        #     print('\n')

                        # elif short_code == 'dc':

                        #     if display_contacts():
                        #         print("Here is a list of all your contacts")
                        #         print('\n')

                        #         for contact in display_contacts():
                        #             print(
                        #                 f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                        #         print('\n')
                        #     else:
                        #         print('\n')
                        #         print("You dont seem to have any contacts saved yet")
                        #         print('\n')

                        # elif short_code == 'fc':

                        #     print("Enter the number you want to search for")

                        #     search_number = input()
                        #     if check_existing_contacts(search_number):
                        #         search_contact = find_contact(search_number)
                        #         print(f"{search_contact.first_name} {search_contact.last_name}")
                        #         print('-' * 20)

                        #         print(f"Phone number.......{search_contact.phone_number}")
                        #         print(f"Email address.......{search_contact.email}")
                        #     else:
                        #         print("That contact does not exist")

                        # elif short_code == "ex":
                        #     print("Bye .......")
                        #     break
                        # else:
                        #     print("I really didn't get that. Please use the short codes")
if __name__=="__main__":
    main()