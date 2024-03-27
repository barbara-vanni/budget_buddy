import requests
from Model.User import User

class Authentication:

    def authenticate(self, mail, password):
        data = {'method': ('READ_TABLE_USER'), 'params': (mail,)}

        if mail == response_data[0][3] and password == response_data[0][4]:
            user = User(response_data[0][1], response_data[0][2], response_data[0][3], response_data[0][4], response_data[0][5], response_data[0][6], response_data[0][7])
            return True, user

        return False, None
    
    def password_enter(password):
        autorized_Special_Char = "!@#$%^&*"
        if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char in autorized_Special_Char for char in password) or not any(char.isdigit() for char in password):
            return False
        return True
    
    def create_account(self, name, surname, mail, password):
        data = {'method': ('CREATE_USER'), 'params': (name, surname, mail, password)}
        user_data = requests.post('http://10.10.107.118:8888', json=data)
        user_data.raise_for_status()