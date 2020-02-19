# -*- coding: utf-8 -*-
from unittest import TestCase
from fizzbuzz import FizzBuzz

class FizzBuzzTest(TestCase):
    def test_returns_number_for_input_not_divisible_by_3_or_5(self):
        self.fizzbuzz = FizzBuzz()
        self.assertEqual('1',  self.fizzbuzz.convert(1))
        self.assertEqual('2',  self.fizzbuzz.convert(2))
        self.assertEqual('4',  self.fizzbuzz.convert(4))
        self.assertEqual('7',  self.fizzbuzz.convert(7))
        self.assertEqual('11', self.fizzbuzz.convert(11))
        self.assertEqual('13', self.fizzbuzz.convert(13))
        self.assertEqual('14', self.fizzbuzz.convert(14))