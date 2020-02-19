# -*- coding: utf-8 -*-

class FizzBuzz:

    def convert(self, number):
        # raise NotImplementedError
        # for number in range(1, 101):
            if number%3 == 0 and number%5 != 0:
                return ("Fizz")
            elif number%3 != 0 and number%5 == 0:
                return("Buzz")
            elif number%3 == 0 and number%5 == 0:
                return("FizzBuzz")
            else:
                return str(number)