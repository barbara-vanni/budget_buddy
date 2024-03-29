from View.RenderTab import RenderTab
from View.Image import Image
from View.Button import Button
from View.Screen import Screen
import tkinter as tk

custom_entries = []

class RenderBudget:
    def __init__(self):
        self.tab_object = RenderTab()

    def render_global_menu(self):
        background_image = Image(self.tab_object.get_canvas(), 0, 0, './assets/images/bcg_menu_global.png')
        self.tab_object.draw_canvas()
        background_image.draw()

        transcation_button= Button(self.tab_object.get_canvas(), 200, 15, "./assets/images/transaction_button.png", None)
        transcation_button.bind('<Button-1>', lambda event: self.render_transaction())

        budget_button = Button(self.tab_object.get_canvas(), 500, 15, "./assets/images/budget_button.png", None)
        budget_button.bind('<Button-1>', lambda event: self.render_budget())

        deconnexion_button = Button(self.tab_object.get_canvas(), 800, 11, "./assets/images/deco_button.png", None)
        deconnexion_button.bind('<Button-1>', lambda event: self.render_deconnexion())

        welcome_label = tk.Label(self.tab_object.get_canvas(), text="Welcome", font=("Helvetica", 16), bg="#0045ab", fg="white")
        welcome_label.place(x=10, y=20)

        self.tab_object.get_screen_object().get_screen().mainloop()
        self.tab_object.get_canvas().update()

    def render_transaction(self):
        self.tab_object.draw_window_canvas()

        background_image = Image(self.tab_object.get_window_canvas(), 0, 0, './assets/images/bcg_window.png')
        background_image.draw()

        transaction_label = tk.Label(self.tab_object.get_window_canvas(), text="Transaction", font=("Helvetica", 20), bg="#0045ab", fg="white")
        transaction_label.place(x=730, y=40)

        # credit_button = Button(self.tab_object.get_window_canvas(), 750, 150, "images/credit_button.png", None)
        # credit_button.bind('<Button-1>', lambda event: self.render_credit())

        # debit_button = Button(self.tab_object.get_window_canvas(), 750, 200, "images/debit_button.png", None)
        # debit_button.bind('<Button-1>', lambda event: self.render_debit())

        # date_button = Button(self.tab_object.get_window_canvas(), 750, 250, "images/date_button.png", None)
        # date_button.bind('<Button-1>', lambda event: self.render_date())

        # category_button = Button(self.tab_object.get_window_canvas(), 750, 300, "images/category_button.png", None)
        # category_button.bind('<Button-1>', lambda event: self.render_category())

        # types_button = Button(self.tab_object.get_window_canvas(), 750, 350, "images/types_button.png", None)
        # types_button.bind('<Button-1>', lambda event: self.render_types())

        # orders_button = Button(self.tab_object.get_window_canvas(), 750, 400, "images/orders_button.png", None)
        # orders_button.bind('<Button-1>', lambda event: self.render_orders())

        # periods_button = Button(self.tab_object.get_window_canvas(), 750, 450, "images/periods_button.png", None)
        # periods_button.bind('<Button-1>', lambda event: self.render_periods())

        self.tab_object.get_screen_object().get_screen().mainloop()
        self.tab_object.get_canvas().update()

    def render_budget(self):
        self.tab_object.draw_window_canvas()

        background_image = Image(self.tab_object.get_window_canvas(), 0, 0, './assets/images/bcg_window.png')
        background_image.draw()

        budget_label = tk.Label(self.tab_object.get_window_canvas(), text="Budget", font=("Helvetica", 20), bg="#0045ab", fg="white")
        budget_label.place(x=760, y=40)

        # soldes_button = Button(self.tab_object.get_window_canvas(), 750, 150, "./assets/images/soldes_button.png", None)
        # soldes_button.bind('<Button-1>', lambda event: self.render_soldes())

        # graphiques_button = Button(self.tab_object.get_window_canvas(), 750, 200, "./assets/images/graphiques_button.png", None)
        # graphiques_button.bind('<Button-1>', lambda event: self.render_graphiques())

        self.tab_object.get_screen_object().get_screen().mainloop()
        self.tab_object.get_canvas().update()

render = RenderBudget()



