from RequestDb import RequestDb
'''
TransactionRepository class is a child class of RequestDb class.
It is used to interact with the transaction table in the database.
'''

class TransactionRepository(RequestDb):
    def __init__(self):
        super().__init__()

    def create_transaction(self, date, description, amount, type, category, id_user):
        '''
        Create a transaction in the database
        '''
        if type == 'credit':
            self.create('transaction', {
                'date': date,
                'description': description,
                'amount': amount,
                'type': 'credit',
                'category': category,
                'id_user': id_user
            })
        elif type == 'debit':
            self.create('transaction', {
                'date': date,
                'description': description,
                'amount': amount,
                'type': 'debit', 
                'category': category,
                'id_user': id_user
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


# transa = TransactionRepository()
# transa.create_transaction('2021-03-10', 'Salaire', 2000, 'credit', 'Salaire', 1)
# transa.create_transaction('2021-03-10', 'Loyer', 500, 'debit', 'Loyer', 1)
# print(transa.read_transaction())
# transa.update_transaction({'amount': 12000.9555}, 'id = 1')
# print(transa.read_transaction())
# transa.delete_transaction('id = 1')
# print(transa.read_transaction())