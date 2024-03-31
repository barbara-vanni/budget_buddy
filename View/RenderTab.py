from View.Entry import CustomEntry
from View.Image import Image
from View.Button import Button
from View.Screen import Screen
from Controler.Budget import Budget
from Model.Transaction import Transaction
import tkinter as tk

custom_entries = []

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
        self.canvas.pack(side = tk.TOP)

    def draw_window_canvas(self):
        self.window_canvas.pack(fill=tk.BOTH, expand=True)
        self.window_canvas.place(x=0, y=64)

    def render(self):
        self.draw_window_canvas()

        date_entry = CustomEntry(self.window_canvas, "Date", 200, 50)
        description_entry = CustomEntry(self.window_canvas, "Description", 200, 150)
        amount_entry = CustomEntry(self.window_canvas, "Amount", 200, 250)
        category_entry = CustomEntry(self.window_canvas, "Category", 200, 350)
        
        custom_entries.append(date_entry, description_entry, amount_entry, category_entry)
        return date_entry, description_entry, amount_entry, category_entry
    
    def render_credit(self):
        date_entry, description_entry, amount_entry, category_entry = self.render()

        types = "credit"
        
        transaction = Transaction(date_entry, description_entry, amount_entry, types, category_entry, 1)

        send_transaction_button = Button(self.window_canvas, 200, 450, './assets/sign_in_button.png', None)
        send_transaction_button.bind('<Button-1>', lambda event: self.budget.create_budget(transaction))
    
    def render_debit(self):
        date_entry, description_entry, amount_entry, category_entry = self.render()

        types = "debit"

        transaction = Transaction(date_entry, description_entry, amount_entry, types, category_entry, 1)

        send_transaction_button = Button(self.window_canvas, 200, 450, './assets/sign_in_button.png', None)
        send_transaction_button.bind('<Button-1>', lambda event: self.budget.create_budget(transaction))

    def render_date(self):

        date_entry = CustomEntry(self.window_canvas, "Date", 50, 50)

        valider = Button(self.window_canvas, 400, 50, './assets/images/validate.png', None)
        valider.bind('<Button-1>', lambda event: self.budget.read_specific_date(1, date_entry))
    
    def render_category(self):
            
        category_entry = CustomEntry(self.window_canvas, "Category", 50, 50)

        valider = Button(self.window_canvas, 400, 50, './assets/images/validate.png', None)
        valider.bind('<Button-1>', lambda event: self.budget.read_specific_category(category_entry, 1))

    def render_types(self):
        types_entry = CustomEntry(self.window_canvas, "Type", 50, 50)

        send_transaction_button = Button(self.window_canvas, 400, 50, './assets/images/validate.png', None)
        # send_transaction_button.bind('<Button-1>', lambda event: self.on_send_transaction_button_click(None, None, None, types_entry, None))
    
    def render_orders(self):

        assend_button = Button(self.window_canvas, 50, 50, './assets/images/assend_button.png', None)
        assend_button.bind('<Button-1>', lambda event: self.on_send_transaction_button_click("assend"))

        descend_button = Button(self.window_canvas, 350, 50, './assets/images/descend_button.png', None)
        descend_button.bind('<Button-1>', lambda event: self.on_send_transaction_button_click("descend"))

    def render_periods(self):

        from_date_entry = CustomEntry(self.window_canvas, "From", 50, 50)
        to_date_entry = CustomEntry(self.window_canvas, "To", 50, 250)

        valider = Button(self.window_canvas, 400, 50, './assets/images/validate.png', None)
        valider.bind('<Button-1>', lambda event: self.on_send_transaction_button_click(from_date_entry, to_date_entry))
    
    def render_soldes(self):
        pass

    def render_graphiques(self):
        pass