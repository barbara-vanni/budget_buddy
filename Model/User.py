class User:
    def __init__(self, name, firstname, mail, password):
        self.name = name
        self.firstname = firstname
        self.mail = mail
        self.password = password

    #getter and setter for name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    #getter and setter for surname
    def get_firstname(self):
        return self.firstname
    def set_firstname(self, firstname):
        self.firstname = firstname

    #getter and setter for mail
    def get_mail(self):
        return self.mail
    def set_mail(self, mail):
        self.mail = mail

    #getter and setter for password
    def get_password(self):
        return self.password
    def set_password(self, password):
        self.password = password
