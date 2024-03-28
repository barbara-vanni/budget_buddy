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
            print(budget.total_account(1))
        else:
            running = False

        transaction_object = Transaction(date, description, amount, types, category, id_user)
        print(vars(transaction_object))
        transaction_repo.set_transaction_list(transaction_object)
        print(transaction_repo.get_transaction_list())
        budget = Budget(transaction_object)
        budget.create_budget()
        # print(budget.total_account(1))
        # print(budget.create_budget(1, '2021-07-07', 'Pv', 1000, 'debit', 'Pv'))
        # print(budget.create_budget(1,'2021-05-05', 'Loyer', 100, 'debit', 'Loyer'))
        # print(budget.read_budget(1))
        # print(budget.debit_credit(1))
        # print(budget.overdraft(1))
        # running = False

except Exception as e:
    print(f"Error: {e}")


        # auth = Authentication()
        # choice = input('Enter your choice: ')
        # if choice == '1':
        #     mail = input('Enter your mail: ')
        #     password = input('Enter your password: ')
        #     print ('mail :', mail, 'password :', password )
        #     if auth.authenticate(mail, password):
        #         print('You are connected')
        #     else:
        #         print('Wrong mail or password')
        # elif choice == '2':
        #     name = input('Enter your name: ')
        #     firstname = input('Enter your firstname: ')
        #     mail = input('Enter your mail: ')
        #     password = input('Enter your password: ')
        #     auth.create_account(name, firstname, mail, password)
        # elif choice == '3':
        #     print('Goodbye')
        #     running = False
        # else:
        #     print('Enter a valid choice')