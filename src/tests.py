#!/usr/bin/env python3

import unittest
import math_lib

class BasicTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_lib.add(5,-5), 0)

    def test_sub(self):
        self.assertEqual(math_lib.sub(99, 99), 0)

    def test_mul(self):
        self.assertEqual(math_lib.mul(5,2), 10)

    def test_abs(self):
        self.assertEqual(math_lib.abs(-100), 100)

    def test_sqrt(self):
        self.assertEqual(math_lib.sqrt(100), 10)

    def test_sqrt_extended(self):
        self.assertEqual(math_lib.sqrt(8, 3), 2)

    def test_pow(self):
        self.assertEqual(math_lib.pow(10), 100)

    def test_pow_extended(self):
        self.assertEqual(math_lib.pow(2, 3), 8)

    def test_fact(self):
        self.assertEqual(math_lib.fact(5), 120)

    def test_sqrt_zero(self):
        self.assertEqual(math_lib.sqrt(0), 0)

    def test_fact_zero(self):
        self.assertEqual(math_lib.fact(0), 1)

    def test_pow_zero(self):
        self.assertEqual(math_lib.pow(5,0), 1)


class ExtendedTests(unittest.TestCase):
    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            math_lib.div(5,0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            math_lib.sqrt(-50)

    def test_sqrt_extended(self):
        with self.assertRaises(ValueError):
            math_lib.sqrt(-5, 4)

    def test_fact_float(self):
        with self.assertRaises(ValueError):
            math_lib.fact(1.56)

    def test_fact_negative(self):
        with self.assertRaises(ValueError):
            math_lib.fact(-50)

    def test_pow(self):
        with self.assertRaises(ValueError):
            math_lib.pow(0,0)


if __name__ == '__main__':
        unittest.main()
