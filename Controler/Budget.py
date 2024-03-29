import requests
from Model.Transaction import Transaction
from Model.TransactionRepository import TransactionRepository

'''
Class Budget :
contains the method create_budget, read_budget, update_budget, delete_budget
'''

class Budget:
    def __init__(self):
        self.__transaction_repo = TransactionRepository()
    
    def get_transaction_repo(self):
        return self.__transaction_repo
    def set_transaction_repo(self, transaction_repo):
        self.__transaction_repo = transaction_repo


    def create_budget(self, transaction_object):
        '''
        method to create a budget
        '''
        self.__transaction_repo.create_transaction(transaction_object)


    def read_budget(self, id_user):
        '''
        method to read a budget
        '''
        transaction_list = []
        user_transactions = self.__transaction_repo.print_user_transactions(id_user)
        for transaction in user_transactions:
            transaction_object = Transaction(transaction[1], transaction[2], transaction[3], transaction[4], transaction[5], transaction[6])
            transaction_list.append(transaction_object)
        return transaction_list

    def total_account(self, id_user):
        '''
        method to calculate the total amount of the account
        '''
        transactions = self.__transaction_repo.read_transaction(conditions=f"id_user = {id_user}")
        total = 0
        for transaction in transactions:
            if transaction[4] == 'credit':
                total += transaction[3]
            elif transaction[4] == 'debit':
                total -= transaction[3]
        return total


    def debit_credit(self, id_user):
        '''
        method to calculate the total amount of the account
        '''
        transactions = self.__transaction_repo.read_transaction(conditions=f"id_user = {id_user}")
        total_credit = 0
        total_debit = 0
        for transaction in transactions:
            if transaction[4] == 'credit':
                total_credit += transaction[3]
            elif transaction[4] == 'debit':
                total_debit += transaction[3]
        return total_credit, total_debit
    
    def overdraft(self, id_user):
        '''
        method to calculate the overdraft of the account
        '''
        total = self.total_account(id_user)
        if total < 0:
            return 'You are in overdraft'
        else:
            return 'You are not in overdraft'

    def read_specific_date(self, id_user, date):
        '''
        method to read a budget by specific date
        '''
        one_date_list = []
        one_date_transactions = self.__transaction_repo.print_specific_date(date, id_user)
        for transaction in one_date_transactions:
            transaction_object = Transaction(transaction[1], transaction[2], transaction[3], transaction[4], transaction[5], transaction[6])
            one_date_list.append(transaction_object)
        return one_date_list
    

    def read_specific_category(self, category, id_user):
        '''
        method to read a budget by specific category
        '''
        category_list = []
        category_transactions = self.__transaction_repo.print_by_category(category, id_user)
        for transaction in category_transactions:
            transaction_object = Transaction(transaction[1], transaction[2], transaction[3], transaction[4], transaction[5], transaction[6])
            category_list.append(transaction_object)
        return category_list

    def read_specific_type(self, types, id_user):
        '''
        method to read a budget by specific type
        '''
        type_list = []
        type_transactions = self.__transaction_repo.print_by_type(types, id_user)
        for transaction in type_transactions:
            transaction_object = Transaction(transaction[1], transaction[2], transaction[3], transaction[4], transaction[5], transaction[6])
            type_list.append(transaction_object)
        return type_list

    def read_by_ascending_money(self, id_user):
        '''
        method to read a budget by ascending order
        '''
        ascending_list = []
        ascending_transactions = self.__transaction_repo.print_by_ascending_money(id_user)
        for transaction in ascending_transactions:
            transaction_object = Transaction(transaction[1], transaction[2], transaction[3], transaction[4], transaction[5], transaction[6])
            ascending_list.append(transaction_object)
        return ascending_list

    def read_by_descending_money(self, id_user):
        '''
        method to read a budget by descending order
        '''
        descending_list = []
        descending_transactions = self.__transaction_repo.print_by_descending_money(id_user)
        for transaction in descending_transactions:
            transaction_object = Transaction(transaction[1], transaction[2], transaction[3], transaction[4], transaction[5], transaction[6])
            descending_list.append(transaction_object)
        return descending_list

    def read_between_dates(self, id_user, date1, date2):
        '''
        method to read a budget by date
        '''
        between_dates = []
        between_dates_transactions = self.__transaction_repo.print_between_dates( date1, date2,id_user)
        for transaction in between_dates_transactions:
            transaction_object = Transaction(transaction[1], transaction[2], transaction[3], transaction[4], transaction[5], transaction[6])
            between_dates.append(transaction_object)
        return between_dates