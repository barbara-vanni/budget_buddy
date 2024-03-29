from View.Entry import CustomEntry
from View.Image import Image
from View.Button import Button
from View.Screen import Screen

custom_entries = []

class RenderAuthentication:
    def __init__(self):
        self.screen_object = Screen()

    def get_screen_object(self):
        return self.screen_object

    def draw_canvas(self):
        self.screen_object.get_canvas().pack()
    
    def render_main_menu(self):
        canvas = self.screen_object.get_canvas()

        for entry in custom_entries:
            entry.destroy_entry()

        background_image = Image(canvas, 0, 0, './assets/bcg_menu.png')
        self.draw_canvas()
        background_image.draw()

        sign_in_button = Button(canvas, 100, 500, './assets/sign_in_button.png', None)
        # sign_in_button.bind('<Button-1>', lambda event: self.render_sign_in(self.screen_object, canvas))

        log_in_button = Button(canvas, 600, 500, './assets/log_in_button.png', None)
        # log_in_button.bind('<Button-1>', lambda event: self.render_log_in(self.screen_object, canvas))

        self.screen_object.get_screen().mainloop()
        canvas.update()

    # def on_real_sign_in_button_click(self, auth, entry1, entry2, entry3, entry4):
    #     auth.create_account(entry1.get_value(), entry2.get_value(), entry3.get_value(), entry4.get_value())
    #     self.render_log_in()

    # def render_sign_in(self, screen, canvas,  event=None):
    #     background_image = Image(canvas, 0, 0, './assets/bcg_signin.png')
    #     background_image.draw()

    #     entry1 = CustomEntry(screen, "Name", x=300, y=141)
    #     entry2 = CustomEntry(screen, "Username", x=300, y=217)
    #     entry3 = CustomEntry(screen, "Email", x=300, y=293)
    #     entry4 = CustomEntry(screen, "Password", x=300, y=369, show='*')

    #     custom_entries.extend([entry1, entry2, entry3, entry4])

    #     real_sign_in_button = Button(canvas, 330, 450, './assets/sign_in_button_2.png', None)
    #     real_sign_in_button.bind('<Button-1>', lambda event: self.on_real_sign_in_button_click(entry1, entry2, entry3, entry4))
    #     screen.mainloop()
    #     canvas.update()
        
    # def check_authenticate(self, mail, password):
    #     return_authenticate = auth.authenticate(mail, password)
    #     if return_authenticate[0] == True:
    #         user = return_authenticate[1]
            
    #         client.connect_to_server('10.10.107.118', 8080)
    #         threading.Thread(target=read_messages_loop).start()
    #         render_chat(user)
    #     else:
    #         print("Authentication failed")

    # def render_log_in(self, screen, canvas, event=None):

    #     for entry in custom_entries:
    #         entry.destroy_entry()

    #     background_image = Image(canvas, 0, 0, './assets/bcg_login.png')
    #     background_image.draw()

    #     entry5 = CustomEntry(screen, "Email", x=300, y=217)
    #     entry6 = CustomEntry(screen, "Password", x=300, y=293)

    #     custom_entries.extend([entry5, entry6])

    #     real_log_in_button = Button(canvas, 340, 360, './assets/log_in_button_2.png', None)
    #     real_log_in_button.bind('<Button-1>', lambda event: self.check_authenticate(entry5.get_value(), entry6.get_value()))

    #     new_here_button = Button(canvas, 269, 430, './assets/new_here_button.png', None)
    #     new_here_button.bind('<Button-1>', self.render_sign_in(screen, canvas))

    #     screen.mainloop()
    #     canvas.update()


auth = RenderAuthentication()