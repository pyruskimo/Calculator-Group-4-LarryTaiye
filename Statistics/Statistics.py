
from Calculator.Calculator import Calculator
# from Statistics.Mean import mean
import statistics


class Statistics(Calculator):

    def mean(self, data):
        self.result = statistics.mean(data) #Updated from mean(data) to statistics.mean(data)
        return self.result

