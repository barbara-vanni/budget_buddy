from View.Entry import CustomEntry
from View.Image import Image
from View.Button import Button
from View.Screen import Screen
from Controler.Budget import Budget
from Model.Transaction import Transaction
import tkinter as tk

custom_entries = []
buttons = []

class RenderTab:
    def __init__(self):
        self.screen_object = Screen()
        self.canvas = self.screen_object.get_canvas()
        self.window_canvas = self.screen_object.get_window_canvas()
        self.budget = Budget()

    def get_screen_object(self):
        return self.screen_object
    
    def get_canvas(self):
        return self.canvas
    
    def get_window_canvas(self):
        return self.window_canvas

    def draw_canvas(self):
        '''
        Draw the canvas of the application
        '''
        self.canvas.pack(side = tk.TOP)

    def draw_window_canvas(self):
        '''
        Draw the window canvas of the application
        '''
        self.window_canvas.pack(fill=tk.BOTH, expand=True)
        self.window_canvas.place(x=0, y=64)

    def destroy_entries(self):
        '''
        Destroy all the entries in the custom_entries list
        '''
        for entry in custom_entries:
            entry.destroy_entry()
    
    def destroy_buttons(self):
        '''
        Destroy all the buttons in the buttons list
        '''
        for button in buttons:
            button.delete()

    def render(self):
        '''
        Render the different entries for the credit and debit transactions
        '''
        self.draw_window_canvas()
        self.destroy_entries()

        # Créer les entrées
        date_entry = CustomEntry(self.window_canvas, "Date", 200, 50)
        description_entry = CustomEntry(self.window_canvas, "Description", 200, 150)
        amount_entry = CustomEntry(self.window_canvas, "Amount", 200, 250)
        category_entry = CustomEntry(self.window_canvas, "Category", 200, 350)

        # Retourner les objets d'entrée
        return date_entry, description_entry, amount_entry, category_entry

    def render_credit(self):
        '''
        Render the credit transaction page
        Create a transaction object and send it to the on_send_transaction_button_click method
        '''
        self.destroy_buttons()
        date_entry, description_entry, amount_entry, category_entry = self.render()

        types = "credit"

        # Fonction pour envoyer la transaction lors de la soumission
        def submit_transaction():
            transaction = Transaction(date_entry.get_value(), description_entry.get_value(), amount_entry.get_value(), types, category_entry.get_value(), 1)
            self.budget.create_budget(transaction)

        # Créer un bouton de soumission
        send_transaction_button = Button(self.window_canvas, 200, 450, './assets/sign_in_button.png', None)
        send_transaction_button.bind('<Button-1>', lambda event: submit_transaction())
        buttons.append(send_transaction_button)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    def render_debit(self):
        '''
        Render the debit transaction page
        Create a transaction object and send it to the on_send_transaction_button_click method
        '''
        self.destroy_buttons()
        date_entry, description_entry, amount_entry, category_entry = self.render()

        types = "debit"

        # Fonction pour envoyer la transaction lors de la soumission
        def submit_transaction(id_name):
            transaction = Transaction(date_entry.get_value(), description_entry.get_value(), amount_entry.get_value(), types, category_entry.get_value(), id_name)
            self.budget.create_budget(transaction)

        # Créer un bouton de soumission
        send_transaction_button = Button(self.window_canvas, 200, 450, './assets/sign_in_button.png', None)
        send_transaction_button.bind('<Button-1>', lambda event: submit_transaction(1))
        buttons.append(send_transaction_button)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    def render_date(self):
        '''
        Render the date page
        send entries to the on_send_transaction_button_click method
        '''
        self.destroy_buttons()
        self.destroy_entries()

        date_entry = CustomEntry(self.window_canvas, "Date", 50, 50)

        def date_validation(id_name):
            transactions = self.budget.read_specific_date(id_name, date_entry.get_value())
            self.render_transaction_table(transactions)

        valider = Button(self.window_canvas, 600, 45, './assets/images/validate.png', None)
        valider.bind('<Button-1>', lambda event: date_validation(1))

        custom_entries.append(date_entry)
        buttons.append(valider)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()
    
    def render_category(self):
        '''
        Render the category page
        send entries to the on_send_transaction_button_click method
        '''

        self.destroy_buttons()
        self.destroy_entries()

        category_entry = CustomEntry(self.window_canvas, "Category", 50, 50)

        def category_validation(id_name):
            transactions = self.budget.read_specific_category(category_entry.get_value(), id_name)
            self.render_transaction_table(transactions)

        valider = Button(self.window_canvas, 600, 45, './assets/images/validate.png', None)
        valider.bind('<Button-1>', lambda event: category_validation(1))

        custom_entries.append(category_entry)
        buttons.append(valider)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    def render_types(self):
        '''
        Render the types page
        send entries to the on_send_transaction_button_click method
        '''

        self.destroy_buttons()
        self.destroy_entries()

        types_entry = CustomEntry(self.window_canvas, "Type", 50, 50)

        def types_validation(id_name):
            transactions = self.budget.read_specific_type(types_entry.get_value(), id_name)
            self.render_transaction_table(transactions)

        send_transaction_button = Button(self.window_canvas, 600, 45, './assets/images/validate.png', None)
        send_transaction_button.bind('<Button-1>', lambda event: types_validation(1))

        custom_entries.append(types_entry)
        buttons.append(send_transaction_button)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()
    
    def render_orders(self):
        '''
        Render the orders page
        send entries to the on_send_transaction_button_click method
        '''

        self.destroy_buttons()
        self.destroy_entries()

        def order_validation(id_user, order):
            if order == "assend":
                transactions = self.budget.read_by_ascending_money(id_user)
                self.render_transaction_table(transactions)
            elif order == "descend":
                transactions = self.budget.read_by_descending_money(id_user)
                self.render_transaction_table(transactions)

        assend_button = Button(self.window_canvas, 50, 50, './assets/images/validate.png', None)
        assend_button.bind('<Button-1>', lambda event: order_validation(1, "assend"))

        descend_button = Button(self.window_canvas, 350, 50, './assets/images/validate.png', None)
        descend_button.bind('<Button-1>', lambda event: order_validation(1, "descend"))

        buttons.extend([assend_button, descend_button])

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    def render_periods(self):
        '''
        Render the periods page
        send entries to the on_send_transaction_button_click method
        '''

        self.destroy_buttons()
        self.destroy_entries()

        from_date_entry = CustomEntry(self.window_canvas, "From", 50, 50)
        to_date_entry = CustomEntry(self.window_canvas, "To", 50, 250)

        def date_to_date_validation(id_name):
            transactions = self.budget.read_between_dates(id_name, from_date_entry.get_value(), to_date_entry.get_value())
            self.render_transaction_table(transactions)

        valider = Button(self.window_canvas, 400, 50, './assets/images/validate.png', None)
        valider.bind('<Button-1>', lambda event: date_to_date_validation(1))

        custom_entries.extend([from_date_entry, to_date_entry])
        buttons.append(valider)

        self.screen_object.get_screen().mainloop()
        self.window_canvas.update()
    
    def render_soldes(self):
        pass

    def render_graphiques(self):
        pass

    def render_transaction_table(self, transactions):
        '''
        Render the transaction table
        Each transactions are received from on_send_transaction_button_click methods       
        Each transaction will be displayed in a row
        '''
        self.draw_window_canvas()

        # Dessiner un en-tête pour le tableau
        headers = ['Date', 'Description', 'Amount', 'Types', 'Category']
        for i, header in enumerate(headers):
            header_label = tk.Label(self.window_canvas, text=header, font=("Helvetica", 12), bg="#0045ab", fg="white")
            header_label.grid(row=0, column=i, padx=5, pady=5)

        # Dessiner les données de transaction
        for i, transaction in enumerate(transactions, start=1):
            tk.Label(self.window_canvas, text=transaction.get_date(), font=("Helvetica", 10)).grid(row=i, column=0, padx=5, pady=5)
            tk.Label(self.window_canvas, text=transaction.get_description(), font=("Helvetica", 10)).grid(row=i, column=1, padx=5, pady=5)
            tk.Label(self.window_canvas, text=transaction.get_amount(), font=("Helvetica", 10)).grid(row=i, column=2, padx=5, pady=5)
            tk.Label(self.window_canvas, text=transaction.get_types(), font=("Helvetica", 10)).grid(row=i, column=3, padx=5, pady=5)
            tk.Label(self.window_canvas, text=transaction.get_category(), font=("Helvetica", 10)).grid(row=i, column=4, padx=5, pady=5)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()