
from Calculator.Calculator import Calculator
# from Statistics.Mean import mean
import statistics
Calculator.Mutiplication import multiplication # Added due to - ModuleNotFoundError: No module named 'Calculator.Mutiplication'

class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

