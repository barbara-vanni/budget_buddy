from Controler.Authentication import Authentication
from Controler.Budget import Budget
from Model.Transaction import Transaction
from Model.TransactionRepository import TransactionRepository

try : 
    running = True

    transaction_repo = TransactionRepository()
    while running :
        print('1. Create Transaction')
        print('2. Read User Transactions')
        print('3. Total Account')
        print('4. Debit Credit')
        print('5. Specific Date')
        print('6. Specific Category')
        print('7. Specific Type')
        print('8. By ascending order')
        print('9. By descending order')
        print('10. Between two dates')
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