class Transaction:
    def __init__(self, request_object, date, description, amount, type, category, id_user):
        self.__request_object = request_object
        self.__date = date
        self.__description = description
        self.__amount = amount
        self.__type = type
        self.__category = category
        self.__id_user = id_user

        def get_request_object(self):
            return self.__request_object
        def set_request_object(self, request_object):
            self.__request_object = request_object
        
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

        def get_type(self):
            return self.__type
        def set_type(self, type):
            self.__type = type

        def get_category(self):
            return self.__category
        def set_category(self, category):
            self.__category = category

        def get_id_user(self):
            return self.__id_user
        def set_id_user(self, id_user):
            self.__id_user = id_user

            