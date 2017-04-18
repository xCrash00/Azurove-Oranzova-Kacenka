#!/usr/bin/env python3

##
# @file tests.py
# File containing unittest tests for mathematical library.
#

import unittest
import math_lib

##
# @brief Class BasicTests - contains easy functional tests
class BasicTests(unittest.TestCase):
	##
	# @brief assertEqual test for math_lib.add
    def test_add(self):
        self.assertEqual(math_lib.add(5,-5), 0)
	##
	# @brief assertEqual test for math_lib.sub
    def test_sub(self):
        self.assertEqual(math_lib.sub(99, 99), 0)
	##
	# @brief assertEqual test for math_lib.mul
    def test_mul(self):
        self.assertEqual(math_lib.mul(5,2), 10)
	##
	# @brief assertEqual test for math_lib.abs
    def test_abs(self):
        self.assertEqual(math_lib.abs(-100), 100)
	##
	# @brief assertEqual test for math_lib.sqrt with a single parameter
    def test_sqrt(self):
        self.assertEqual(math_lib.sqrt(100), 10)
	##
	# @brief assertEqual test for math_lib.sqrt with two parameters
    def test_sqrt_extended(self):
        self.assertEqual(math_lib.sqrt(8, 3), 2)
	##
	# @brief assertEqual test for math_lib.pow wit a single parameter
    def test_pow(self):
        self.assertEqual(math_lib.pow(10), 100)
	##
	# @brief assertEqual test for math_lib.pow with two parameters
    def test_pow_extended(self):
        self.assertEqual(math_lib.pow(2, 3), 8)
	##
	# @brief assertEqual test for math_lib.fact
    def test_fact(self):
        self.assertEqual(math_lib.fact(5), 120)
	##
	# @brief assertEqual test for math_lib.sqrt with argument 0
    def test_sqrt_zero(self):
        self.assertEqual(math_lib.sqrt(0), 0)
	##
	# @brief assertEqual test for math_lib.fact with argument 0
    def test_fact_zero(self):
        self.assertEqual(math_lib.fact(0), 1)
	##
	# @brief assertEqual test for math_lib.pow with second argument 0
    def test_pow_zero(self):
        self.assertEqual(math_lib.pow(5,0), 1)

##
# @brief Class BasicTests - contains tests for exceptions and mathematical errors
class ExtendedTests(unittest.TestCase):
	##
	# @brief tests if division by zero rasies ValueError
    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            math_lib.div(5,0)
	##
	# @brief tests if argument lower than 0 in sqrt function raises ValueError
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            math_lib.sqrt(-50)
	##
	# @brief tests if argument lower than 0 in sqrt function raises ValueError with second parameter
    def test_sqrt_extended(self):
        with self.assertRaises(ValueError):
            math_lib.sqrt(-5, 4)
	##
	# @brief tests if non-decimal part in argument of math_lib.fact raises ValueError
    def test_fact_float(self):
        with self.assertRaises(ValueError):
            math_lib.fact(1.56)
	##
	# @brief tests if a negative number as an argument of math_lib.fact raises ValueError
    def test_fact_negative(self):
        with self.assertRaises(ValueError):
            math_lib.fact(-50)
	##
	# @brief tests if 0 to the power of 0 raises ValueError
    def test_pow(self):
        with self.assertRaises(ValueError):
            math_lib.pow(0,0)


if __name__ == '__main__':
        unittest.main()
