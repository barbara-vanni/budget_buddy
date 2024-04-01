from View.Entry import CustomEntry
from View.Image import Image
from View.Button import Button
from View.Screen import Screen
from Controler.Authentication import Authentication
from View.menu_current_render import *
from View.RenderBudgetGlobal import RenderBudget


class RenderAuthentication:
    def __init__(self):
        self.screen_object = Screen()
        self.canvas = self.screen_object.get_canvas()
        self.custom_entries = []
        self.authentication = Authentication()

    def get_screen_object(self):
        return self.screen_object

    def draw_canvas(self):
        self.screen_object.get_canvas().pack()
    
    def render_main_menu(self):

        for entry in self.custom_entries:
            entry.destroy_entry()

        background_image = Image(self.canvas, 0, 0, './assets/bcg_menu.png')
        self.draw_canvas()
        background_image.draw()

        sign_in_button = Button(self.canvas, 50, 500, './assets/sign_in_button.png', None)
        sign_in_button.bind('<Button-1>', lambda event: self.render_sign_in())

        log_in_button = Button(self.canvas, 580, 500, './assets/log_in_button.png', None)
        log_in_button.bind('<Button-1>', lambda event: self.render_log_in())

        self.screen_object.get_screen().mainloop()
        self.canvas.update()


    def check_sign_in(self, entry1, entry2, entry3, entry4):
        name = entry1.get_value()
        username = entry2.get_value()
        email = entry3.get_value()
        password = entry4.get_value()

        print("check_auth", name, username, email, password)
        if self.authentication.create_account(name, username, email, password):
            self.render_log_in()
            print("Account created")
        else:
            print("Password not valid")            

    def render_sign_in(self):

        for entry in self.custom_entries:
            entry.destroy_entry()

        background_image = Image(self.canvas, 0, 0, './assets/bcg_sign_menu.png')
        background_image.draw()

        entry1 = CustomEntry(self.canvas, "Name", x=300, y=141)
        entry2 = CustomEntry(self.canvas, "Username", x=300, y=217)
        entry3 = CustomEntry(self.canvas, "Email", x=300, y=293)
        entry4 = CustomEntry(self.canvas, "Password", x=300, y=369, show='*')


        self.custom_entries.extend([entry1, entry2, entry3, entry4])

        real_sign_in_button = Button(self.canvas, 330, 450, './assets/sign_in_button_page.png', None)
        real_sign_in_button.bind('<Button-1>', lambda event: self.check_sign_in(entry1, entry2, entry3, entry4))
        
        self.screen_object.get_screen().mainloop()
        self.canvas.update()

    def check_authenticate(self, entry5, entry6):
        email = entry5
        password = entry6
        if self.authentication.authenticate(email, password):
            print("Connected")
            if self.screen_object.get_screen().winfo_exists():
                self.screen_object.get_screen().destroy()
            budget_menu = RenderBudget()
            set_state(budget_menu.render_global_menu())
        else:
            print("Wrong mail or password")

    def render_log_in(self):

        for entry in self.custom_entries:
            entry.destroy_entry()

        background_image = Image(self.canvas, 0, 0, './assets/bcg_log_menu.png')
        background_image.draw()

        entry5 = CustomEntry(self.canvas, "Email", x=300, y=195)
        entry6 = CustomEntry(self.canvas, "Password", x=300, y=283, show='*')

        self.custom_entries.extend([entry5, entry6])

        real_log_in_button = Button(self.canvas, 340, 360, './assets/log_in_button_page.png', None)
        real_log_in_button.bind('<Button-1>', lambda event: self.check_authenticate(entry5.get_value(), entry6.get_value()))

        new_here_button = Button(self.canvas, 485, 452, './assets/sign_in_button_log_page.png', None)
        new_here_button.bind('<Button-1>', lambda event : self.render_sign_in())

        self.screen_object.get_screen().mainloop()
        self.canvas.update()


# auth = RenderAuthentication()