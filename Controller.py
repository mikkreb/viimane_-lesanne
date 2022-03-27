from View import *
from Model import *

class Controller:
    def __init__(self):
        self.view = View()
        
    def main(self):
        self.view.main()