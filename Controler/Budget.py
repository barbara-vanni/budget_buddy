import requests
from Model.Transaction import Transaction
from Model.TransactionRepository import TransactionRepository

'''
Class Budget :
contains the method create_budget, read_budget, update_budget, delete_budget
'''

class Budget:
    def __init__(self, transaction_object):
        self.__transaction_object = transaction_object
        self.__transaction_repo = TransactionRepository()


    def create_budget(self):
        '''
        method to create a budget
        '''
        self.__transaction_repo.create_transaction(self.__transaction_object)
        self.__transaction_repo.set_transaction_list(self.__transaction_object)


    def read_budget(self, id_user):
        '''
        method to read a budget
        '''

        transactions = self.transaction_repo.read_transaction(conditions=f"id_user = {id_user}")
        return transactions








    def total_account(self, id_user):
        '''
        method to calculate the total amount of the account
        '''
        transactions = self.transaction_repo.read_transaction(conditions=f"id_user = {id_user}")
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
        transactions = self.transaction_repo.read_transaction(conditions=f"id_user = {id_user}")
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

############################################################

    def print_specific_date(self, date, id_user):
        '''
        Print all transactions for a specific date
        '''
        return self.read_transaction(f'date = "{date}" AND id_user = {id_user}')


    def print_by_category(self, category, id_user):
        '''
        Print all transactions by category
        '''
        return self.read_transaction(f'category = "{category}" AND id_user = {id_user}')


    def print_by_type(self, type, id_user):
        '''
        Print all transactions by type
        '''
        return self.read_transaction(f'type = "{type}" AND id_user = {id_user}')


    def print_by_ascending_money(self, id_user):
        '''
        Print all transactions by ascending money
        '''
        return self.read_transaction(f'id_user = {id_user} ORDER BY amount ASC')


    def print_by_descending_money(self, id_user):
        '''
        Print all transactions by descending money
        '''
        return self.read_transaction(f'id_user = {id_user} ORDER BY amount DESC')


    def print_between_dates(self, start_date, end_date, id_user):
        '''
        Print all transactions between two dates
        '''
        return self.read_transaction(f'date BETWEEN "{start_date}" AND "{end_date}" AND id_user = {id_user}')

