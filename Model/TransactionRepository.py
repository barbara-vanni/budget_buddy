from Model.RequestDb import RequestDb
from Model.Transaction import Transaction   
'''
TransactionRepository class is a child class of RequestDb class.
It is used to interact with the transaction table in the database.
'''

class TransactionRepository(RequestDb):
    def __init__(self):
        super().__init__()
        self.transaction_list = []

    # Getters and Setters for transaction_list
    def get_transaction_list(self):
        return self.transaction_list
    def set_transaction_list(self, transaction_object):
        self.transaction_list.append(transaction_object)

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
        self.set_transaction_list(transaction_object)
        # print(self.transaction_list)


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


    