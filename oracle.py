import random

class Oracle():
    def __init__(self):
        self.number = random.random()*100
    
    def is_greater(self, guess):
        """
        Return True if my hidden number is greater than guess, and False otherwise
        """
        return guess < self.number

    def reveal(self):
        """
        Reveal the saved hidden number
        """
        return self.number



