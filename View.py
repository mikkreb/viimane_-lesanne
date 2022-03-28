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
        self.geometry('640x320')
        self.resizable(False, False)
        self.title('Vinge matemaatika mäng!')
        
        # Executing create_xxxxx_frame functions and giving them variables
        self.top_frame = self.create_top_frame()
        self.middle_frame = self.create_middle_frame()
        self.bottom_frame = self.create_bottom_frame()
        
        # Widgets
        self.create_newGameButtons()
        self.wordInput, self.button = self.create_userinput()
        self.labelQuestion, self.labelResult, self.labelCorrect = self.create_infoLabels()
        
    def main(self):
        self.mainloop()
        
    # Frames
    def create_top_frame(self):
        'Creates top frame'
        frame = Frame(self)
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_middle_frame(self):
        'Creates middle frame'
        frame = Frame(self)
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_bottom_frame(self):
        'Creates bottom frame'
        frame = Frame(self)
        frame.pack(expand=True, fill='both')
        return frame
    
    # Widgets
    def create_userinput(self):
        'Creates a label, entry and a button on the bottom frame for user input'
        labelInfo = Label(self.bottom_frame, text = 'Sisestage vastus:', font=self.defaultFontBold)
        labelInfo.grid(row=0, column=0, pady=5, padx=5)
        
        wordInput = Entry(self.bottom_frame, textvariable=self.userinput, justify='center', font=self.defaultFontStyle)
        wordInput.grid(row=0, column=1, padx=5, pady=5)
        
        button = Button(self.bottom_frame, text='Vasta', font=self.defaultFontStyle, state=DISABLED,
                        command=lambda:self.controller.btn_answer_click())
        button.grid(row=0, column=2, padx=5, pady=5)
    
        return wordInput, button
    
    # Buttons for starting a new game with a specified gamemode
    def create_newGameButtons(self):
        'Creates buttons for starting new game on the top frame'
        info = Label(self.top_frame, text='Valige mida soovite mängida:', font=self.defaultFontStyle)
        info.grid(row=0, column=0, padx=5, pady=5)
        
        addition = Button(self.top_frame, text='Liitmine', font=self.defaultFontStyle,
                          command=lambda:self.controller.btn_addition_click())
        addition.grid(row=0, column=1, padx=5,pady=5)
        
        subtraction = Button(self.top_frame, text='Lahutamine', font=self.defaultFontStyle,
                             command=lambda:self.controller.btn_subtract_click())
        subtraction.grid(row=0, column=2, padx=5, pady=5)
        
        multiply = Button(self.top_frame, text='Korrutamine', font=self.defaultFontStyle
                          ,command=lambda:self.controller.btn_multiply_click())
        multiply.grid(row=0, column=3, padx=5, pady=5)
        
        division = Button(self.top_frame, text='Jagamine', font=self.defaultFontStyle,
                          command=lambda:self.controller.btn_divide_click())
        division.grid(row=0, column=4, padx=5, pady=5)
        

    def create_infoLabels(self):
        'Displays the math problem and feedback about user input'
        labelQuestion = Label(self.middle_frame, text='Mängu pole veel alustatud!', font=self.bigFontStyle)
        labelQuestion.pack()
        
        labelResult = Label(self.middle_frame, text='', font=self.smallerBigFontStyle)
        labelResult.pack()
        
        labelCorrect = Label(self.middle_frame, text='', font=self.smallerBigFontStyle)
        labelCorrect.pack()
        
        return labelQuestion, labelResult, labelCorrect