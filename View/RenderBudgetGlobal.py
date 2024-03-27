import tkinter as tk
from Bouton import Button
from Image import Image
from Entry import Entry

class RenderBudget:
    def __init__(self):
        self.__screen = tk.Tk()
        self.__width = 900
        self.__height = 700
        self.__canvas = None
        self.__button = []
        self.__render_dictionnary = {
            0: self.render_transaction(),
            1: self.render_budget(),
            2 : self.render_deconnexion(),
            3 : self.render_credit(),
            4 : self.render_debit(),
            5 : self.render_date(),
            6 : self.render_category(),
            7 : self.render_types(),
            8 : self.render_order(),
            9 : self.render_from_to(),
            10 : self.render_budget_states(),
            11 : self.render_budget_grafics()
            }
    
    def get_button(self):
        return self.__button

    def draw_canvas(self, fisrt_name, last_name):
        self.__screen.title(f"Budget {fisrt_name}, {last_name}")
        self.__canvas = tk.Canvas(self.__screen, width=self.__width, height=self.__height)
        self.__canvas.pack()
    
    def draw_background_image(self):
        background_image = Image(self.__canvas, 0, 0, './assets/images/logo_20.png')
        background_image.draw()

    def horizontal_menu_button(self):
        for j in range(3):
            horizontal_button = Button(self.__canvas, 0 + 300 * j, 0, './assets/images/nav_bar_button.png', None)
            self.__button.append(horizontal_button)
    
    def transactions_menu_button(self):
        for i in range(7):
            lateral_button = Button(self.__canvas, 750, 175 + 75 * i, './assets/images/lateral_button.png', None)
            self.__button.append(lateral_button)


    def budget_menu_button(self):
        for i in range(2):
            lateral_button = Button(self.__canvas, 750, 175 + 75 * i, './assets/images/lateral_button.png', None)
            self.__button.append(lateral_button)

    def draw_menu_button(self):
        self.horizontal_menu_button()
        self.lateral_menu_button()
        for button in self.__button:
            button.bind('<Button-1>', lambda event: self.change_render())
        
    def render_transaction(self):
        print("transaction")

    def render_budget(self):
        print("budget")

    def render_deconnexion(self):
        print("deconnexion")

    def render_credit(self):
        print("credit")

    def render_debit(self):
        print("debit")

    def render_date(self):
        print("date")

    def render_category(self):
        print("category")

    def render_types(self):
        print("types")

    def render_order(self):
        print("order")

    def render_from_to(self):
        print("from_to")

    def render_budget_states(self):
        print("states")

    def render_budget_grafics(self):
        print("graphics")
    
    def change_render(self, indice):
        if indice in self.__render_dictionnary:
            set_current_nav_state(self.__render_dictionnary[indice])



running = True
draw = False
render = RenderBudget()
current_state = render.render_transaction()

def get_current_state():
    return current_state
def set_current_nav_state(new_render):
    current_state = new_render
    return current_state

while running:
    if draw == False:
        render.draw_canvas("Yrles", "Anthony")
        render.draw_background_image()
        render.draw_menu_button()
        draw = True


