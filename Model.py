import pathlib
import os
from random import randrange
from random import randint

class Model:
    def __init__(self):
        self.mathproblem = "" # The math problem shown on screen set by set_xxxxx_problem() functions
        self.user_answer = None # Users answer to the math problem
        self.failcounter = 0 # How many wrong answers were given by the user
        self.correctcounter = 0 # How many correct answers were given by the user
        self.answer = 0 # Correct answer set by set_xxxxx_problem() functions
        
        # These two lines make it possible to run on GNU/Linux distributions
        self.myfolder = pathlib.Path(__file__).parent.resolve() # Where the project is located
        self.dst = os.path.join(self.myfolder, 'scores.txt') # Save path for storing scores
        
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
            self.answer = answer
            self.mathproblem = problem
        else:
            problem = str(b) + ' - ' + str(a)
            answer = a - b
            self.answer = answer
            self.mathproblem = problem
        
    def new_multiply_game(self):
        self.get_random_multiply_problem()