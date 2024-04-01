from View.RenderTab import *
from View.Image import Image
from View.Button import Button
from View.Screen import Screen
import tkinter as tk

class RenderBudget:
    def __init__(self, user_id):
        self.tab_object = RenderTab(user_id)
        self.screen_object = Screen()
        self.canvas = self.screen_object.get_canvas()


    def get_screen_object(self):
        return self.screen_object

    def draw_canvas(self):
        self.canvas.pack()

    # def draw_canvas_window(self):
    #     self.screen_object.get_window_canvas().pack()

    def render_global_menu(self):
        '''
        Render the global navigation menu of the application
        '''
        self.tab_object.destroy_all()

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
        '''
        Render the transaction page button page
        each button will redirect to a specific page
        of the RenderTab object
        '''
        self.tab_object.destroy_all()

        self.tab_object.draw_window_canvas()

        background_image = Image(self.tab_object.get_window_canvas(), 0, 0, './assets/images/bcg_window.png')
        background_image.draw()

        transaction_label = tk.Label(self.tab_object.get_window_canvas(), text="Transaction", font=("Helvetica", 20), bg="#0045ab", fg="white")
        transaction_label.place(x=730, y=40)

        credit_button = Button(self.tab_object.get_window_canvas(), 725, 160, "./assets/images/credit_button.png", None)
        credit_button.bind('<Button-1>', lambda event: self.tab_object.render_expense())

        date_button = Button(self.tab_object.get_window_canvas(), 725, 220, "./assets/images/date_button.png", None)
        date_button.bind('<Button-1>', lambda event: self.tab_object.render_date())

        category_button = Button(self.tab_object.get_window_canvas(), 725, 280, "./assets/images/category_button.png", None)
        category_button.bind('<Button-1>', lambda event: self.tab_object.render_category())

        types_button = Button(self.tab_object.get_window_canvas(), 725, 340, "./assets/images/type_button.png", None)
        types_button.bind('<Button-1>', lambda event: self.tab_object.render_types())

        orders_button = Button(self.tab_object.get_window_canvas(), 725, 400, "./assets/images/amount_sort_button.png", None)
        orders_button.bind('<Button-1>', lambda event: self.tab_object.render_orders())

        periods_button = Button(self.tab_object.get_window_canvas(), 725, 460, "./assets/images/date_sort_button.png", None)
        periods_button.bind('<Button-1>', lambda event: self.tab_object.render_periods())

        labels.append(transaction_label)

        self.tab_object.get_screen_object().get_screen().mainloop()
        self.tab_object.get_canvas().update()

    def render_budget(self):
        '''
        Render the budget page button page
        each button will redirect to a specific page
        of the RenderTab object
        '''
        self.tab_object.destroy_all()
        
        self.tab_object.draw_window_canvas()

        background_image = Image(self.tab_object.get_window_canvas(), 0, 0, './assets/images/bcg_window.png')
        background_image.draw()

        budget_label = tk.Label(self.tab_object.get_window_canvas(), text="Budget", font=("Helvetica", 20), bg="#0045ab", fg="white")
        budget_label.place(x=760, y=40)

        soldes_button = Button(self.tab_object.get_window_canvas(), 725, 160, "./assets/images/balance_button.png", None)
        soldes_button.bind('<Button-1>', lambda event: self.tab_object.render_soldes())

        graphiques_button = Button(self.tab_object.get_window_canvas(), 725, 220, "./assets/images/graph_button.png", None)
        graphiques_button.bind('<Button-1>', lambda event: self.tab_object.render_graphic())

        deco_button_budget = Button(self.tab_object.get_window_canvas(), 725, 340, "./assets/images/deco_button_budget.png", None)

        labels.extend([budget_label])

        self.tab_object.get_screen_object().get_screen().mainloop()
        self.tab_object.get_canvas().update()

render = RenderBudget(1)



