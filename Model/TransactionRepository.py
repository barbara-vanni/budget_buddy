from Model.RequestDb import RequestDb
'''
TransactionRepository class is a child class of RequestDb class.
It is used to interact with the transaction table in the database.
'''

class TransactionRepository(RequestDb):
    def __init__(self):
        super().__init__()

    def create_transaction(self, transaction_object):
        '''
        Create a transaction in the database
        '''
        if transaction_object.get_types() == 'credit':
            self.create('transaction', {
                'date': transaction_object.get_date(),
                'description': transaction_object.get_description(),
                'amount': transaction_object.get_amount(),
                'types': 'credit',
                'category': transaction_object.get_category(),
                'id_user': transaction_object.get_id_user()
            })
        elif transaction_object.get_types() == 'debit':
            self.create('transaction', {
                'date': transaction_object.get_date(),
                'description': transaction_object.get_description(),
                'amount': transaction_object.get_amount(),
                'types': 'debit', 
                'category': transaction_object.get_category(),
                'id_user': transaction_object.get_id_user()
            })
        else:
            print('Type must be credit or debit')


    def read_transaction(self, conditions=None):
        '''
        Read transaction from the database
        '''
        return self.read('transaction', conditions)


    def update_transaction(self, data, conditions=None):
        '''
        Update transaction in the database
        '''
        self.update('transaction', data, conditions)


    def delete_transaction(self, conditions):
        '''
        Delete transaction from the database
        '''
        self.delete('transaction', conditions)

    
    def print_user_transactions(self, id_user):
        '''
        Print all transactions for a specific user
        '''
        return self.read_transaction(f'id_user = {id_user}')


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


    def print_by_type(self, types, id_user):
        '''
        Print all transactions by types
        '''
        return self.read_transaction(f'types = "{types}" AND id_user = {id_user}')


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
