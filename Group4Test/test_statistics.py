import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 4.25)

    def test_median_calculator(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, 4.25)  
        
     def test_mode_calculator(self):
        median = self.statistics.mode(self.testData)
        self.assertEqual(mode, 4.25)   
        
     def test_variance_calculator(self):
        median = self.statistics.variance(self.testData)
        self.assertEqual(variance, 4.25)       
        
     def test_stdev_calculator(self):
        median = self.statistics.stdev(self.testData)
        self.assertEqual(stdev, 4.25)        

     def test_zscore_calculator(self):
        median = self.statistics.zscore(self.testData)
        self.assertEqual(zscore, 4.25)          

if __name__ == '__main__':
    unittest.main()
