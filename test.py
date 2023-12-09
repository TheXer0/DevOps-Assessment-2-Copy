import unittest

def calculate_sum(a, b):..............
    return a + b

def check_even_odd(sum):
    if sum % 2 == 0:
        return "Even"
    else:
        return "Odd"

class TestSumFunction(unittest.TestCase):

    def test_sum_even(self):
        # Test case 1: Testing if the sum of two even numbers is even
        result = calculate_sum(4, 6)
        self.assertEqual(result % 2, 0)

    def test_sum_odd(self):
        # Test case 2: Testing if the sum of an odd and even number is odd
        result = calculate_sum(3, 4)
        self.assertEqual(result % 2, 1)

    def test_sum_zero(self):
        # Test case 3: Testing if the sum of zero and a number is the number itself
        result = calculate_sum(0, 8)
        self.assertEqual(result, 8)

    def test_sum_negative(self):
        # Test case 4: Testing if the sum of a negative and a positive number is correct
        result = calculate_sum(-5, 10)
        self.assertEqual(result, 5)

    def test_sum_large_numbers(self):
        # Test case 5: Testing if the sum of large numbers is correct
        result = calculate_sum(1000000000, 2000000000)
        self.assertEqual(result, 3000000000)

if __name__ == '__main__':
    unittest.main()