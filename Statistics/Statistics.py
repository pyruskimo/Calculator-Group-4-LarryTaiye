from Calculator.Calculator import Calculator
from Statistics import Mean 
from Statistics.Median import Median
from Statistics.Mode import Mode
from Statistics.stdev import stdev
from Statistics.zscore import zscore


class Statistics(Calculator):

    def mean(self, data):
        self.result = Statistics.Mean(data)
        return self.result
        
    def median(self, data):
        self.result = Statistics.median(data)
        return self.result  

    def mode(self, data):
        self.result = Statistics.mode(data)
        return self.result     
        
    def stdev(self, data):
        self.result = Statistics.stdev(data)
        return self.result  

    def zscore(self, data):
        self.result = Statistics.zscore(data)
        return self.result         
        
