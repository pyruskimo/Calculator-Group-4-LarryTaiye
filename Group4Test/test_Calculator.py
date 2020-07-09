import unittest
import math

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader("Group4Test/Group4Data/subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
            
    def test_addition(self):
        test_data = CsvReader("Group4Test/Group4Data/addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)    
            
    def test_multiplication(self):
        test_data = CsvReader("Group4Test/Group4Data/multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
            
    def test_division(self):
        test_data = CsvReader("Group4Test/Group4Data/division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))         
            
    def test_square(self):
        test_data = CsvReader("Group4Test/Group4Data/square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(row['Value 1'], result)
            self.assertEqual(self.calculator.result, result)        

    # Old values = def test_sqrt(self):
    def test_sqrt(self):
        test_data = CsvReader("Group4Test/Group4Data/squareroot.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(row['Value 1'], result)
            self.assertEqual(self.calculator.result, result)              
            
            
    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
