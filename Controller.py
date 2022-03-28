from View import *
from Model import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.gamemode = 0 # Gamemode 1-addition 2-subtraction 3-multiply 4-division
        
    def main(self):
        # Executes the main window function presnt in View.py
        self.view.main()
    
    def btn_addition_click(self):
        'When clicked on button Korruta'
        self.gamemode = 1
        self.model.new_game()
        self.model.get_random_addition_problem()
        self.view.labelQuestion.configure(text=self.model.mathproblem)
        self.view.button.configure(state=NORMAL)
    
    # Gamemode 2
    def btn_subtract_click(self):
        'When clicked on button Korruta'
        self.gamemode = 2
        self.model.new_game()
        self.model.get_random_subtraction_problem()
        self.view.labelQuestion.configure(text=self.model.mathproblem)
        self.view.button.configure(state=NORMAL)
    
    # Gamemode 3
    def btn_multiply_click(self):
        'When clicked on button Korruta'
        self.gamemode = 3
        self.model.new_game()
        self.model.get_random_multiply_problem()
        self.view.labelQuestion.configure(text=self.model.mathproblem)
        self.view.button.configure(state=NORMAL)

    # Gamemode 4
    def btn_divide_click(self):
        'When clicked on button Korruta'
        self.gamemode = 4
        self.model.new_game()
        self.model.get_random_division_problem()
        self.view.labelQuestion.configure(text=self.model.mathproblem)
        self.view.button.configure(state=NORMAL)
        
    def btn_answer_click(self):
        'When clicked on button Vasta'
        if self.model.isNumber(self.view.wordInput.get()) == True:
            self.model.get_userinput(self.view.wordInput.get())
            if self.gamemode == 1:
                self.model.get_random_addition_problem()
            if self.gamemode == 2:
                self.model.get_random_subtraction_problem()
            if self.gamemode == 3:
                self.model.get_random_multiply_problem()
            if self.gamemode == 4:
                self.model.get_random_division_problem()
            self.view.labelResult.configure(text='Valesti ' + str(self.model.failcounter) + ' küsimust')
            self.view.labelQuestion.configure(text=self.model.mathproblem)
        else:
            self.view.labelResult.configure(text='Sisestage ainult täisarve!')
        self.view.wordInput.delete(0,'end')