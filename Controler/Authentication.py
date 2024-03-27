import requests
from Model.User import User
from Model.UserRepository import UserRepository
import hashlib

''' Class Authentication : 
contains the method authenticate, create_account '''

class Authentication:
    def __init__(self):
        self.user_repo = UserRepository()

    def authenticate(self, mail, password):
        '''
        method for authentication: check the mail input
        if user exist, check the input password 
        '''
        user_data = self.user_repo.read_user(conditions=f"mail = '{mail}'")
        # if the user exist in the database
        if user_data:
            # collect the hashed password from the Db
            hashed_password_db = user_data[0]['password']

            # Hash the password give by the user 
            password_bytes = password.encode('utf-8')
            hash_password = hashlib.sha256()
            hash_password.update(password_bytes)
            hashed_password_input = hash_password.hexdigest()

            # Compare the hashed password of the db and the one we just hash
            if hashed_password_input == hashed_password_db:
                return True
        return False   

    def password_enter(self, password):
        '''
        method for password verification: check if the password contains at least 8 characters, 1 uppercase, 1 lowercase, 1 digit and 1 special character
        '''
        autorized_Special_Char = "!@#$%^&*"
        if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char in autorized_Special_Char for char in password) or not any(char.isdigit() for char in password):
            return False
        return True
    
    def create_account(self, name, firstname, mail, password):
        '''
        method for account creation: check the password input first 
        '''
        check_password = self.password_enter(password)
        if check_password == True :
            self.user_repo.create_user(name, firstname, mail, password)
            User(name, firstname, mail, password)
        else :
            print('Enter a valid password')