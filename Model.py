import pathlib
import os
from random import randrange
from random import randint

class Model:
    def __init__(self):
        self.mathproblem = '' # The math problem shown on screen set by set_xxxxx_problem() functions
        self.failcounter = 0 # How many wrong answers were given by the user
        self.answer = 0 # Correct answer set by set_xxxxx_problem() functions
        self.correctcounter = 0
        
    # https://stackoverflow.com/questions/46822789/python-generating-random-even-numbers-using-list-comprehension
    def even_number_generator(self, lim):
        while True:
            yield randrange(2,lim,2)
    #print(next(even_number_generator(lim)))

    # Generate a random division math problem
    def get_random_division_problem(self):
        while True:
            a = next(self.even_number_generator(100))
            b = next(self.even_number_generator(100))
            try:
                if a % b == 0:
                    problem = str(a) + ' / ' + str(b)
                    answer = a / b
                    self.answer = answer
                    self.mathproblem = problem
                    break
            except ZeroDivisionError:
                continue
    
    def get_random_multiply_problem(self):
        a = randint(0,100)
        b = randint(0,100)
        problem = str(a) + ' * ' + str(b)
        answer = a * b
        self.answer = answer
        self.mathproblem = problem
    
    def get_random_addition_problem(self):
        a = randint(0,100)
        b = randint(0,100)
        problem = str(a) + ' + ' + str(b)
        answer = a + b
        self.answer = answer
        self.mathproblem = problem
    
    def get_random_subtraction_problem(self):
        a = randint(0,100)
        b = randint(0,100)
        if a >= b:
            problem = str(a) + ' - ' + str(b)
            answer = a - b
            self.answer = str(answer)
            self.mathproblem = problem
        else:
            problem = str(b) + ' - ' + str(a)
            answer = b - a
            self.answer = answer
            self.mathproblem = problem
        
    def new_game(self):
        self.failcounter = 0
        self.correctcounter = 0
        
    def compare_answers(self, value):
        'Returns True if user answer is correct'
        if int(self.answer) == int(value):
            self.correctcounter += 1
            return True
        else:
            return False
        
    def get_userinput(self, value):
        if self.compare_answers(value) == False:
            self.failcounter += 1
            #print(self.failcounter) test
    
    def isNumber(self, value):
        try:
            int(value)
            return True
        except:
            return False