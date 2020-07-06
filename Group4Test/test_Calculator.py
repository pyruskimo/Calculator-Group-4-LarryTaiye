import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

   
    def test_subtract_method_calculator(self):
        test_data = CsvReader("Group4Test/Group4Data/subtraction.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1']), row['Value 2']), float(row['Result'])
            self.assertEqual(self.calculator.result, float(row['Result']))
        
    def test_add_method_calculator(self):
        test_data = CsvReader("Group4Test/Group4Data/addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1']), row['Value 2']), (row['Result'])
            self.assertEqual(self.calculator.result, (row['Result']))

   
    def test_multiply_method_calculator(self):
        test_data = CsvReader("Group4Test/Group4Data/multiplication.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1']), row['Value 2']), float(row['Result'])
            self.assertEqual(self.calculator.result, float(row['Result']))
            
    def test_divide_method_calculator(self):
        test_data = CsvReader("Group4Test/Group4Data/division.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1']), row['Value 2']), float(row['Result'])
            self.assertEqual(self.calculator.result, float(row['Result']))     
            
    def test_sq_method_calculator(self):
        test_data = CsvReader("Group4Test/Group4Data/square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sq(row['Value 1']), (row['Result']))
            self.assertEqual(self.calculator.result, (row['Result']))
       
    def test_sqrt_method_calculator(self):
        test_data = CsvReader("Group4Test/Group4Data/squareroot.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), float(row['Result'])
            self.assertEqual(self.calculator.result, float(row['Result']))          
       
    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
