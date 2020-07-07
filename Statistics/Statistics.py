
from Calculator.Calculator import Calculator
# from Statistics.Mean import mean
import statistics


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

