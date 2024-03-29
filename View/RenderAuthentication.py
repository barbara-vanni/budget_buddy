from View.Entry import CustomEntry
from View.Image import Image
from View.Button import Button
from View.Screen import Screen


class RenderAuthentication:
    def __init__(self):
        self.screen_object = Screen()
        self.canvas = self.screen_object.get_canvas()
        self.custom_entries = []

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

    # def on_real_sign_in_button_click(self, auth, entry1, entry2, entry3, entry4):
    #     auth.create_account(entry1.get_value(), entry2.get_value(), entry3.get_value(), entry4.get_value())
    #     self.render_log_in()

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
        # real_sign_in_button.bind('<Button-1>', lambda event: self.on_real_sign_in_button_click(entry1, entry2, entry3, entry4))
        
        self.screen_object.get_screen().mainloop()
        self.canvas.update()
        
    # def check_authenticate(self, mail, password):
    #     return_authenticate = auth.authenticate(mail, password)
    #     if return_authenticate[0] == True:
    #         user = return_authenticate[1]
            
    #         client.connect_to_server('10.10.107.118', 8080)
    #         threading.Thread(target=read_messages_loop).start()
    #         render_chat(user)
    #     else:
    #         print("Authentication failed")

    def render_log_in(self):

        for entry in self.custom_entries:
            entry.destroy_entry()

        background_image = Image(self.canvas, 0, 0, './assets/bcg_log_menu.png')
        background_image.draw()

        entry5 = CustomEntry(self.canvas, "Email", x=300, y=195)
        entry6 = CustomEntry(self.canvas, "Password", x=300, y=283)

        self.custom_entries.extend([entry5, entry6])

        real_log_in_button = Button(self.canvas, 340, 360, './assets/log_in_button_page.png', None)
        # real_log_in_button.bind('<Button-1>', lambda event: self.check_authenticate(entry5.get_value(), entry6.get_value()))

        new_here_button = Button(self.canvas, 485, 452, './assets/sign_in_button_log_page.png', None)
        new_here_button.bind('<Button-1>', lambda event : self.render_sign_in())

        self.screen_object.get_screen().mainloop()
        self.canvas.update()


auth = RenderAuthentication()