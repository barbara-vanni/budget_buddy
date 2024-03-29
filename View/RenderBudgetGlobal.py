from View.Entry import CustomEntry
from View.Image import Image
from View.Button import Button
from View.Screen import Screen
import tkinter as tk

custom_entries = []

class RenderBudget:
    def __init__(self):
        self.screen_object = Screen()
        self.canvas = self.screen_object.get_canvas()
        # self.window_canvas = self.screen_object.get_window_canvas()

    def get_screen_object(self):
        return self.screen_object

    def draw_canvas(self):
        self.canvas.pack()

    # def draw_canvas_window(self):
    #     self.screen_object.get_window_canvas().pack()

    def render_global_menu(self):

        for entry in custom_entries:
            entry.destroy_entry()
        
        background_image = Image(self.canvas, 0, 0, './assets/images/bcg_menu_global.png')
        self.draw_canvas()
        background_image.draw()

        transcation_button= Button(self.canvas, 300, 0, "./assets/images/transaction_button.png", None)
        transcation_button.bind('<Button-1>', lambda event: self.render_transaction())

        budget_button = Button(self.canvas, 600, 0, "./assets/images/budget_button.png", None)
        budget_button.bind('<Button-1>', lambda event: self.render_budget())

        deconnexion_button = Button(self.canvas, 800, 0, "./assets/images/deco_button.png", None)
        deconnexion_button.bind('<Button-1>', lambda event: self.render_deconnexion())

        welcome_label = tk.Label(self.canvas, text="Welcome", font=("Helvetica", 16), bg="#0045ab", fg="white")
        welcome_label.place(x=10, y=20)

        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    # def render_transaction(self):
    #     self.draw_window_canvas()

    #     transaction_label = tk.Label(self.canvas_window, text="Transaction", font=("Helvetica", 16), bg="white")
    #     transaction_label.place(x=770, y=0)

    #     credit_button = Button(self.canvas_window, 750, 150, "images/credit_button.png", None)
    #     credit_button.bind('<Button-1>', lambda event: self.render_credit())

    #     debit_button = Button(self.canvas_window, 750, 200, "images/debit_button.png", None)
    #     debit_button.bind('<Button-1>', lambda event: self.render_debit())

    #     date_button = Button(self.canvas_window, 750, 250, "images/date_button.png", None)
    #     date_button.bind('<Button-1>', lambda event: self.render_date())

    #     category_button = Button(self.canvas_window, 750, 300, "images/category_button.png", None)
    #     category_button.bind('<Button-1>', lambda event: self.render_category())

    #     types_button = Button(self.canvas_window, 750, 350, "images/types_button.png", None)
    #     types_button.bind('<Button-1>', lambda event: self.render_types())

    #     orders_button = Button(self.canvas_window, 750, 400, "images/orders_button.png", None)
    #     orders_button.bind('<Button-1>', lambda event: self.render_orders())

    #     periods_button = Button(self.canvas_window, 750, 450, "images/periods_button.png", None)
    #     periods_button.bind('<Button-1>', lambda event: self.render_periods())

    #     self.screen_object.get_screen().mainloop()

        
render = RenderBudget()



