from Controler.Authentication import Authentication
from Controler.Budget import Budget
from Model.Transaction import Transaction
from Model.TransactionRepository import TransactionRepository

try : 
    running = True
    # transaction_repo = TransactionRepository()
    budget = Budget()
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
            transaction_object = Transaction(date, description, amount, types, category, id_user)
            budget.create_budget(transaction_object)

        elif choice == '2':
            id_user = input('Enter your user: ')
            user_transaction_list = budget.read_budget(id_user)

        elif choice == '3':
            id_user = input('Enter your user: ')
            total = budget.total_account(id_user)
            overdraft = budget.overdraft(id_user)
            print(total)
            print(overdraft)

        elif choice == '4':
            id_user = input('Enter your user: ')
            total = budget.debit_credit(id_user)
            print(total)

        elif choice == '5':
            id_user = input('Enter your user: ')
            date = input('Enter your date(YYYY-MM-DD): ')
            one_date_list = budget.read_specific_date(id_user, date)
            print(one_date_list)

        elif choice == '6':
            id_user = input('Enter your user: ')
            category = input('Enter your category: ')
            category_list = budget.read_specific_category(category, id_user)
            print(category_list)

        elif choice == '7':
            id_user = input('Enter your user: ')
            types = input('Enter your type: ')
            type_list = budget.read_specific_type(types, id_user)
            print(type_list)

        elif choice == '8':
            id_user = input('Enter your user: ')
            ascending_list = budget.read_by_ascending_money(id_user)
            print(ascending_list)

        elif choice == '9':
            id_user = input('Enter your user: ')
            descending_list = budget.read_by_descending_money(id_user)
            print(descending_list)

        elif choice == '10':
            id_user = input('Enter your user: ')
            date1 = input('Enter your first date(YYYY-MM-DD): ')
            date2 = input('Enter your second date(YYYY-MM-DD): ')
            between_dates = budget.read_between_dates(id_user, date1, date2)
            print(between_dates)

        else:
            running = False

        # running = False

except Exception as e:
    print(f"Error: {e}")