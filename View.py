from tkinter import *
import tkinter.font as tkFont

class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.userinput = StringVar()
        # Font syles
        self.bigFontStyle = tkFont.Font(family='Courier', size=18, weight='bold')
        self.smallerBigFontStyle = tkFont.Font(family='Courier', size=14, weight='bold')
        self.defaultFontStyle = tkFont.Font(family='Verdana', size=10)
        self.defaultFontBold = tkFont.Font(family='Verdana', size=10, weight='bold')
        
        # Main window
        self.geometry('640x480')
        self.resizable(False, False)
        self.title('Vinge matemaatika mäng!')
        
        # Executing create_xxxxx_frame functions and giving them variables
        self.top_frame = self.create_top_frame()
        self.middle_frame = self.create_middle_frame()
        self.bottom_frame = self.create_bottom_frame()
        
        # Widgets
        self.create_newGameButtons()
        self.wordInput = self.create_userinput()
        self.create_infoLabels()
        
    def main(self):
        self.mainloop()
        
    # Frames
    def create_top_frame(self):
        frame = Frame(self, bg='blue')
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_middle_frame(self):
        frame = Frame(self, bg='grey')
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_bottom_frame(self):
        frame = Frame(self, bg='yellow')
        frame.pack(expand=True, fill='both')
        return frame
    
    # Widgets
    def create_userinput(self):
        labelInfo = Label(self.bottom_frame, text = 'Sisestage vastus:', font=self.defaultFontBold)
        labelInfo.grid(row=0, column=0, pady=5, padx=5)
        
        wordInput = Entry(self.bottom_frame, textvariable=self.userinput, justify='center', font=self.defaultFontStyle)
        wordInput.grid(row=0, column=1, padx=5, pady=5)
        
        button = Button(self.bottom_frame, text='Vasta', font=self.defaultFontStyle)
        button.grid(row=0, column=2, padx=5, pady=5)
    
        return wordInput
    
    def create_newGameButtons(self):
        info = Label(self.top_frame, text='Valige mida soovite mängida:', font=self.defaultFontStyle)
        info.grid(row=0, column=0, padx=5, pady=5)
        
        addition = Button(self.top_frame, text='Liitmine', font=self.defaultFontStyle)
        addition.grid(row=0, column=1, padx=5,pady=5)
        
        subtraction = Button(self.top_frame, text='Lahutamine', font=self.defaultFontStyle)
        subtraction.grid(row=0, column=2, padx=5, pady=5)
        
        multiply = Button(self.top_frame, text='Korrutamine', font=self.defaultFontStyle)
        multiply.grid(row=0, column=3, padx=5, pady=5)
        
        division = Button(self.top_frame, text='Jagamine', font=self.defaultFontStyle)
        division.grid(row=0, column=4, padx=5, pady=5)
        
        return addition, subtraction, multiply, division

    def create_infoLabels(self):
        labelQuestion = Label(self.middle_frame, text='Sisestage vastus:', font=self.bigFontStyle)
        labelQuestion.pack()
        
        labelResult = Label(self.middle_frame, text='Correct!', font=self.smallerBigFontStyle)
        labelResult.pack()