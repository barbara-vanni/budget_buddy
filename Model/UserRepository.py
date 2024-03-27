from Model.RequestDb import RequestDb
import hashlib

class UserRepository(RequestDb):
    def __init__(self):
        super().__init__()

    def create_user(self, name, firstname, mail, password):
        password_bytes = password.encode('utf-8')
        hash_password = hashlib.sha256()
        hash_password.update(password_bytes)
        hashed_password = hash_password.hexdigest()
        self.create('user', {'name': name, 'firstname': firstname, 'mail': mail, 'password': hashed_password})

    def read_user(self, conditions=None):
        return self.read('user', conditions)

    def update_user(self, data, conditions=None):
        if 'password' in data:
            password_bytes = data['password'].encode('utf-8')
            hash_password = hashlib.sha256()
            hash_password.update(password_bytes)
            data['password'] = hash_password.hexdigest()
        self.update('user', data, conditions)
    
    def delete_user(self, conditions):
        self.delete('user', conditions)

# user_repo = UserRepository()
# # user_repo.create_user(name='Jean', firstname='Jacques', email='jj@gmail.com', password='pass147258+')
# user_repo.read_user()
# print(user_repo.read_user())
# user_repo.update_user({'name': 'Jean', 'firstname': 'Jacques', 'email': 'jb@gmail.com', 'password': '7258+'})
# print(user_repo.read_user())
# user_repo.delete_user('email = "jb@gmail.com"')
# print(user_repo.read_user())


