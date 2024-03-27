from Controler.Authentication import Authentication
# from Controler.Budget import Budget

try : 
    running = True

    while running :
        print('1. Login')
        print('2. Create an account')
        print('3. Quit')
        auth = Authentication()
        choice = input('Enter your choice: ')
        if choice == '1':
            mail = input('Enter your mail: ')
            password = input('Enter your password: ')
            print ('mail :', mail, 'password :', password )
            if auth.authenticate(mail, password):
                print('You are connected')
            else:
                print('Wrong mail or password')
        elif choice == '2':
            name = input('Enter your name: ')
            firstname = input('Enter your firstname: ')
            mail = input('Enter your mail: ')
            password = input('Enter your password: ')
            auth.create_account(name, firstname, mail, password)
        elif choice == '3':
            print('Goodbye')
            running = False
        else:
            print('Enter a valid choice')

except Exception as e:
    print(f"Error: {e}")

