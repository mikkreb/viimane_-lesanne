from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk

class View:
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.userinput = StringVar()
        # Font syles
        self.bigFontStyle = tkFont.Font(family='Courier', size=18, weight='bold')
        self.defaultFontStyle = tkFont.Font(family='Verdana', size=10)
        self.defaultFontBold = tkFont.Font(family='Verdana', size=10, weight='bold')
        
        # Main window
        self.geometry('640x480')
        self.resizable(False, False)
        self.title('.db editor')
        
        # Frames
        
        # Widgets
        
    def main(self):
        self.mainloop()