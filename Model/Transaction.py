class Transaction:
    def __init__(self, date, description, amount, types, category, id_user):
        self.__date = date
        self.__description = description
        self.__amount = amount
        self.__types = types
        self.__category = category
        self.__id_user = id_user
        
    def get_date(self):
        return self.__date
    def set_date(self, date):
        self.__date = date

    def get_description(self):
        return self.__description
    def set_description(self, description):
        self.__description = description

    def get_amount(self):
        return self.__amount
    def set_amount(self, amount):
        self.__amount = amount

    def get_types(self):
        return self.__types
    def set_types(self, types):
        self.__types = types

    def get_category(self):
        return self.__category
    def set_category(self, category):
        self.__category = category

    def get_id_user(self):
        return self.__id_user
    def set_id_user(self, id_user):
        self.__id_user = id_user

            