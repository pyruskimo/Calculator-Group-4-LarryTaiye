from Calculator.Addition import subtraction
from Calculator.Subtraction import addition
from Calculator.Division import addition
from Calculator.Multiplication import addition


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result
        
    def divide(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = subtraction(a, b)
        return self.result    





