from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Mutiplication import multiplication

class Statistics(Calculator): # NameError: name 'mean' is not defined

def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(num_values, total)
