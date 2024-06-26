from View.Entry import CustomEntry
from View.Image import Image
from View.Button import Button
from View.Screen import Screen
from Controler.Budget import Budget
from Model.Transaction import Transaction
from tkinter import StringVar, OptionMenu
import tkinter as tk
import matplotlib.pyplot as plt

custom_entries = []
buttons = []
labels = []
dropdowns = []
images = []

class RenderTab:
    def __init__(self, screen, user_id):
        self.screen_object = screen
        self.canvas = self.screen_object.get_canvas()
        self.window_canvas = self.screen_object.get_window_canvas()
        self.budget = Budget()
        self.user_id = user_id

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
    
    def destroy_labels(self):
        '''
        Destroy all the labels in the labels list
        '''
        for label in labels:
            label.destroy()

    def destroy_dropdowns(self):
        '''
        Destroy all the dropdowns in the dropdowns list
        '''
        for dropdown in dropdowns:
            dropdown.destroy()

    def destroy_images(self):
        '''
        Destroy all the images in the images list
        '''
        for image in images:
            image.delete()

    def destroy_all(self):
        '''
        Destroy all the entries, buttons and labels
        '''
        self.destroy_entries()
        self.destroy_buttons()
        self.destroy_labels()
        self.destroy_dropdowns()
        self.destroy_images()

    def render(self):
        '''
        Render the different entries for the credit and debit transactions
        '''
        self.draw_window_canvas()
        self.destroy_entries()

        transaction_label = tk.Label(self.window_canvas, text="Transaction", font=("Helvetica", 20), bg="#0045ab", fg="white")
        transaction_label.place(x=730, y=40)

        date_entry = CustomEntry(self.window_canvas, "Date (YYYY-MM-DD)", 200, 120)
        description_entry = CustomEntry(self.window_canvas, "Description", 200, 210)
        amount_entry = CustomEntry(self.window_canvas, "Amount", 200, 300)

        # Create a dropdown menu for the type of transaction
        type_options = ["Debit", "Credit"]
        type_variable = StringVar(self.window_canvas)
        type_variable.set("Choose your type")
        types_dropdown = OptionMenu(self.window_canvas, type_variable, *type_options)
        types_dropdown.config(bg="#0045ab", width=18, font=("Arial", 20), relief="flat", fg="white", activebackground="#0045ab", activeforeground="white", highlightthickness=0, bd=0, anchor="w")
        types_dropdown.place(x=200, y=30)

        #Create a dropdown menu for the category of the transaction
        category_options = ["Salaire", "Loyer", "Alimentation", "Loisirs", "Autres"]
        category_variable = StringVar(self.window_canvas)
        category_variable.set("Choose your category")
        category_dropdown = OptionMenu(self.window_canvas, category_variable, *category_options)
        category_dropdown.config(bg="#0045ab", width=18, font=("Arial", 20), relief="flat", fg="white", activebackground="#0045ab", activeforeground="white", highlightthickness=0, bd=0, anchor="w")
        category_dropdown.place(x=200, y=390)

        custom_entries.extend([date_entry, description_entry, amount_entry])
        dropdowns.extend([types_dropdown, category_dropdown])
        labels.append(transaction_label)

        return date_entry, description_entry, amount_entry, type_variable, category_variable

    def render_expense(self):
        '''
        Render the credit transaction page
        Create a transaction object and send it to the on_send_transaction_button_click method
        '''
        self.destroy_buttons()
        self.destroy_all()
        date_entry, description_entry, amount_entry, type_variable, category_variable = self.render()

        def submit_transaction():
            if type_variable.get() == "Debit":
                type_value = "debit"
            elif type_variable.get() == "Credit":
                type_value = "credit"

            if category_variable.get() == "Salaire":
                category_value = "salaire"
            elif category_variable.get() == "Loyer":
                category_value = "loyer"
            elif category_variable.get() == "Alimentation":
                category_value = "alimentation"
            elif category_variable.get() == "Loisirs":
                category_value = "loisirs"
            elif category_variable.get() == "Autres":
                category_value = "autres"

            transaction = Transaction(date_entry.get_value(), description_entry.get_value(), amount_entry.get_value(), type_value, category_value, self.user_id)
            self.budget.create_budget(transaction)
            if self.budget.total_account(1) < 0:
                register_label = tk.Label(self.window_canvas, text="Your Transaction have been register", font=("Helvetica", 22), fg="yellow", bg="#0045ab")
                register_label.place(x=50, y=455)
                overdraft_label = tk.Label(self.window_canvas, text="You're in Overdaft", font=("Helvetica", 22), fg="#0045ab", bg="red")
                overdraft_label.place(x=50, y=495)
                labels.extend([register_label, overdraft_label])
            else:
                register_label = tk.Label(self.window_canvas, text="Your Transaction have been register", font=("Helvetica", 22), fg="yellow", bg="#0045ab")
                register_label.place(x=50, y=455)
                labels.append(register_label)

        send_transaction_button = Button(self.window_canvas, 460, 450, './assets/images/validate.png', None)
        send_transaction_button.bind('<Button-1>', lambda event: submit_transaction())
        buttons.append(send_transaction_button)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    def render_date(self):
        '''
        Render the date page
        send entries to the on_send_transaction_button_click method
        '''
        self.destroy_all()

        date_entry = CustomEntry(self.window_canvas, "Date (YYYY-MM-DD)", 200, 270)

        transaction_label = tk.Label(self.window_canvas, text="Transaction", font=("Helvetica", 20), bg="#0045ab", fg="white")
        transaction_label.place(x=730, y=40)

        def date_validation(id_name):
            transactions = self.budget.read_specific_date(id_name, date_entry.get_value())
            self.render_transaction_table(transactions)

        valider = Button(self.window_canvas, 450, 320, './assets/images/validate.png', None)
        valider.bind('<Button-1>', lambda event: date_validation(self.user_id))

        custom_entries.append(date_entry)
        buttons.append(valider)
        labels.append(transaction_label)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()
    
    def render_category(self):
        '''
        Render the category page
        send entries to the on_send_transaction_button_click method
        '''

        self.destroy_all()

        transaction_label = tk.Label(self.window_canvas, text="Transaction", font=("Helvetica", 20), bg="#0045ab", fg="white")
        transaction_label.place(x=730, y=40)

        #Create a dropdown menu for the category of the transaction
        category_options = ["Salaire", "Loyer", "Alimentation", "Loisirs", "Autres"]
        category_variable = StringVar(self.window_canvas)
        category_variable.set("Choose your category")
        category_dropdown = OptionMenu(self.window_canvas, category_variable, *category_options)
        category_dropdown.config(bg="#0045ab", width=18, font=("Arial", 20), relief="flat", fg="white", activebackground="#0045ab", activeforeground="white", highlightthickness=0, bd=0, anchor="w")
        category_dropdown.place(x=200, y=270)

        def category_validation(id_name):
            if category_variable.get() == "Salaire":
                category_value = "salaire"
            elif category_variable.get() == "Loyer":
                category_value = "loyer"
            elif category_variable.get() == "Alimentation":
                category_value = "alimentation"
            elif category_variable.get() == "Loisirs":
                category_value = "loisirs"
            elif category_variable.get() == "Autres":
                category_value = "autres"
            transactions = self.budget.read_specific_category(category_value, id_name)
            self.render_transaction_table(transactions)

        valider = Button(self.window_canvas, 450, 320, './assets/images/validate.png', None)
        valider.bind('<Button-1>', lambda event: category_validation(self.user_id))

        buttons.append(valider)
        dropdowns.append(category_dropdown)
        labels.append(transaction_label)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    def render_types(self):
        '''
        Render the types page
        send entries to the on_send_transaction_button_click method
        '''

        self.destroy_all()

        transaction_label = tk.Label(self.window_canvas, text="Transaction", font=("Helvetica", 20), bg="#0045ab", fg="white")
        transaction_label.place(x=730, y=40)

        # Create a dropdown menu for the type of transaction
        type_options = ["Debit", "Credit"]
        type_variable = StringVar(self.window_canvas)
        type_variable.set("Choose your type")
        types_dropdown = OptionMenu(self.window_canvas, type_variable, *type_options)
        types_dropdown.config(bg="#0045ab", width=18, font=("Arial", 20), relief="flat", fg="white", activebackground="#0045ab", activeforeground="white", highlightthickness=0, bd=0, anchor="w")
        types_dropdown.place(x=200, y=270)

        def types_validation(id_name):
            if type_variable.get() == "Debit":
                type_value = "debit"
            elif type_variable.get() == "Credit":
                type_value = "credit"
            transactions = self.budget.read_specific_type(type_value, id_name)
            self.render_transaction_table(transactions)

        send_transaction_button = Button(self.window_canvas, 450, 320, './assets/images/validate.png', None)
        send_transaction_button.bind('<Button-1>', lambda event: types_validation(self.user_id))

        buttons.append(send_transaction_button)
        dropdowns.append(types_dropdown)
        labels.append(transaction_label)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()
    
    def render_orders(self):
        '''
        Render the orders page
        send entries to the on_send_transaction_button_click method
        '''

        self.destroy_all()

        transaction_label = tk.Label(self.window_canvas, text="Transaction", font=("Helvetica", 20), bg="#0045ab", fg="white")
        transaction_label.place(x=730, y=40)

        def order_validation(id_user, order):
            if order == "assend":
                transactions = self.budget.read_by_ascending_money(id_user)
                self.render_transaction_table(transactions)
            elif order == "descend":
                transactions = self.budget.read_by_descending_money(id_user)
                self.render_transaction_table(transactions)

        assend_image = Image(self.window_canvas, 250, 200, './assets/images/ascending.png')
        assend_button = Button(self.window_canvas, 450, 200, './assets/images/validate.png', None)
        assend_button.bind('<Button-1>', lambda event: order_validation(self.user_id, "assend"))

        descend_image = Image(self.window_canvas, 250, 300, './assets/images/descending.png')
        descend_button = Button(self.window_canvas,450, 300, './assets/images/validate.png', None)
        descend_button.bind('<Button-1>', lambda event: order_validation(self.user_id, "descend"))

        images.extend([assend_image, descend_image])
        buttons.extend([assend_button, descend_button])
        labels.append(transaction_label)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    def render_periods(self):
        '''
        Render the periods page
        send entries to the on_send_transaction_button_click method
        '''

        self.destroy_all()

        transaction_label = tk.Label(self.window_canvas, text="Transaction", font=("Helvetica", 20), bg="#0045ab", fg="white")
        transaction_label.place(x=730, y=40)

        from_date_entry = CustomEntry(self.window_canvas, "From (YYYY-MM-DD)", 200, 230)
        to_date_entry = CustomEntry(self.window_canvas, "To (YYYY-MM-DD)", 200, 300)

        def date_to_date_validation(id_name):
            transactions = self.budget.read_between_dates(id_name, from_date_entry.get_value(), to_date_entry.get_value())
            self.render_transaction_table(transactions)

        valider = Button(self.window_canvas, 450, 350, './assets/images/validate.png', None)
        valider.bind('<Button-1>', lambda event: date_to_date_validation(self.user_id))

        custom_entries.extend([from_date_entry, to_date_entry])
        buttons.append(valider)
        labels.append(transaction_label)

        self.screen_object.get_screen().mainloop()
        self.window_canvas.update()
    
    def render_soldes(self):
        '''
        Render the soldes page
        '''
        self.destroy_all()

        total_credit, total_debit = self.budget.debit_credit(self.user_id)

        budget_label = tk.Label(self.window_canvas, text="Budget", font=("Helvetica", 20), bg="#0045ab", fg="white")
        budget_label.place(x=760, y=40)

        total_credit_label = tk.Label(self.window_canvas, text="Total Credit: " + str(total_credit), font=("Helvetica", 22), fg="white", bg="#0045ab")
        total_credit_label.place(x=200, y=210)

        total_debit_label = tk.Label(self.window_canvas, text="Total Debit: " + str(total_debit), font=("Helvetica", 22), fg="white", bg="#0045ab")
        total_debit_label.place(x=200, y=315)

        total = self.budget.total_account(self.user_id)
        if total < 0:
            total_label = tk.Label(self.window_canvas, text="Total: " + str(total), font=("Helvetica", 22), fg="#0045ab", bg="red")
            overdraft_label = tk.Label(self.window_canvas, text="You're in Overdaft", font=("Helvetica", 22), fg="#0045ab", bg="red")
            total_label.place(x=200, y=420)
            overdraft_label.place(x=200, y=470)
            labels.extend([budget_label, total_credit_label, total_debit_label, total_label, overdraft_label])
        else:
            total_label = tk.Label(self.window_canvas, text="Total: " + str(total), font=("Helvetica", 22), fg="yellow", bg="#0045ab")
            total_label.place(x=200, y=420)
            labels.extend([budget_label, total_credit_label, total_debit_label, total_label])

        self.screen_object.get_screen().mainloop()
        self.window_canvas.update()

    def render_graphic(self):
        '''
        Render the graphic page
        All the transactions are hardcoded
        '''
        self.destroy_all()

        budget_label = tk.Label(self.window_canvas, text="Budget", font=("Helvetica", 20), bg="#0045ab", fg="white")
        budget_label.place(x=760, y=40)

        labels = 'Salaire', 'Loyer', 'Courses', 'Loisirs', 'Autres'
        sizes = self.budget.graphic_budget(self.user_id)
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
        explode = (0.1, 0, 0, 0, 0)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.title('Graphique des dépenses')
        plt.show()

        labels.append(budget_label)
      
    def render_transaction_table(self, transactions):
        '''
        Render the transaction table
        Each transactions are received from on_send_transaction_button_click methods       
        Each transaction will be displayed in a row
        '''
        transparent_window = tk.Toplevel(self.window_canvas)

        table_canvas = tk.Canvas(transparent_window, bg="gray", bd=0, highlightthickness=0)
        table_canvas.pack(fill=tk.BOTH, expand=True)

        headers = ['Date', 'Description', 'Amount', 'Types', 'Category']
        for i, header in enumerate(headers):
            header_label = tk.Label(table_canvas, text=header, font=("Helvetica", 18), fg="black")
            header_label.grid(row=0, column=i, padx=5, pady=5)

        for i, transaction in enumerate(transactions, start=1):
            tk.Label(table_canvas, text=transaction.get_date(), font=("Helvetica", 18)).grid(row=i, column=0, padx=5, pady=5)
            tk.Label(table_canvas, text=transaction.get_description(), font=("Helvetica", 18)).grid(row=i, column=1, padx=5, pady=5)
            tk.Label(table_canvas, text=transaction.get_amount(), font=("Helvetica", 18)).grid(row=i, column=2, padx=5, pady=5)
            tk.Label(table_canvas, text=transaction.get_types(), font=("Helvetica", 18)).grid(row=i, column=3, padx=5, pady=5)
            tk.Label(table_canvas, text=transaction.get_category(), font=("Helvetica", 18)).grid(row=i, column=4, padx=5, pady=5)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()