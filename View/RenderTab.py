from View.Entry import CustomEntry
from View.Image import Image
from View.Button import Button
from View.Screen import Screen
import tkinter as tk

class RenderTab:
    def __init__(self):
        self.screen_object = Screen()
        self.canvas = self.screen_object.get_canvas()
        self.window_canvas = self.screen_object.get_window_canvas()

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