from random import randint, choice

class Die:
    def __init__(self):
        self.faces = ["dot", "dot", "dot", "L", "C", "R"]
    
    def roll(self):
        return choice(self.faces)