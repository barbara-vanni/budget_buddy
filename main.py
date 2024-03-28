from Controler.Authentication import Authentication
from Controler.Budget import Budget
from Model.Transaction import Transaction
from Model.TransactionRepository import TransactionRepository

try : 
    running = True

    transaction_repo = TransactionRepository()
    while running :
        print('1. User connection')
        print('2. Date')
        print('3. Description')
        print('4. Amount')
        print('5. Types')
        print('6. Category')
        choice = input('Enter your choice: ')
        if choice == '1':
            id_user = input('Enter your user: ')
            date = input('Enter your date(YYYY-MM-DD): ')
            description = input('Enter your description: ')
            amount = input('Enter your amount: ')
            types = input('Enter your type: ')
            category = input('Enter your category: ')

        elif choice == '2':
            id_user = input('Enter your user: ')
            transaction_object = Transaction(None, None, None, None, None, id_user)
            print(transaction_repo.read_transaction(id_user, transaction_object))
        else:
            running = False

        transaction_object = Transaction(date, description, amount, types, category, id_user)
        transaction_repo.set_transaction_list(transaction_object)
        budget = Budget(transaction_object)
        budget.create_budget()

        # running = False

except Exception as e:
    print(f"Error: {e}")