from View import *
from Model import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        
    def main(self):
        # Executes the main window function presnt in View.py
        self.view.main()