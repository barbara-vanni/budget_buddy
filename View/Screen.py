import tkinter as tk

class Screen():
    def __init__(self) -> None:
        self.__screen = tk.Tk()
        self.__width = 900
        self.__height = 600
        self.__canvas = tk.Canvas(self.__screen, width=self.__width, height=self.__height)
        self.__window_canvas = tk.Canvas(self.__screen, width=self.__width, height=self.__height)

    def get_screen(self):
        return self.__screen
    
    def get_canvas(self):
        return self.__canvas

    def get_window_canvas(self):
        return self.__window_canvas
        