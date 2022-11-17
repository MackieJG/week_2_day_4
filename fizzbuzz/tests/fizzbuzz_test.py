import unittest

from modules.fizzbuzz import fizzbuzz
class FizzbuzzTest(unittest.TestCase):

    def test_number_divisible_by_3(self):
        input_number = 9
        expected_output = "Fizz"
        actual_output = fizzbuzz(input_number)
        self.assertEqual(expected_output, actual_output)

    def test_nunber_divisible_by_5(self):
        input_number = 10
        expected_output = "Buzz"
        actual_output = fizzbuzz(input_number)
        self.assertEqual(expected_output, actual_output)

    def test_number_divisible_by_3_and_5(self):
        input_number = 15
        expected_output = "FizzBuzz"
        actual_output = fizzbuzz(input_number)
        self.assertEqual(expected_output, actual_output)

    def test_number_not_divisible_by_3_or_5(self):
        input_number = 8
        expected_output = "8"
        actual_output = fizzbuzz(input_number)
        self.assertEqual(expected_output, actual_output)