from Calculator.Calculator import Calculator
from Statistics.Mean import 
from Statistics.Median import 
from Statistics.Mode import 
from Statistics.stdev import


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result
        
    def median(self, data):
        self.result = median(data)
        return self.result  

    def mode(self, data):
        self.result = mode(data)
        return self.result     
        
    def stdev(self, data):
        self.result = stdev(data)
        return self.result  
