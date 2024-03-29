from Model.RequestDb import RequestDb
import hashlib
'''
UserRepository class is a child class of RequestDb class. 
It is used to interact with the user table in the database.
'''


class UserRepository(RequestDb):
    def __init__(self):
        super().__init__()

    def create_user(self, name, firstname, mail, password):
        '''
        Create a user in the database
        '''
        password_bytes = password.encode('utf-8')
        hash_password = hashlib.sha256()
        hash_password.update(password_bytes)
        hashed_password = hash_password.hexdigest()
        self.create('user', {'name': name, 'firstname': firstname, 'mail': mail, 'password': hashed_password})


    def read_user(self, conditions=None):
        '''
        Read user from the database
        '''
        return self.read('user', conditions)


    def update_user(self, data, conditions=None):
        '''
        Update user in the database
        '''
        if 'password' in data:
            password_bytes = data['password'].encode('utf-8')
            hash_password = hashlib.sha256()
            hash_password.update(password_bytes)
            data['password'] = hash_password.hexdigest()
        self.update('user', data, conditions)
    

    def delete_user(self, conditions):
        '''
        Delete user from the database
        '''
        self.delete('user', conditions)

