#!/usr/bin/env python3
##
# @file math_lib.py
# File containing definitions of mathematical functions.
#

##
# @brief function that adds two numbers
# @param a first number
# @param b second number
# @return sum of a and b
def add(a,b):
    return a + b

##
# @brief function that subtracts two numbers
# @param a first number
# @param b second number
# @return difference of a and b
def sub(a,b):
    return a - b
##
# @brief function that multiplies one number by another
# @param a first number
# @param b second number
# @return a multiplied by b
def mul(a,b):
    return a * b

##
# @brief function that divides one number by another
# @param a first number
# @param b second number
# @raises ValueError if b equals 0
# @return a divided by b
def div(a,b):
    if b == 0:
        raise ValueError
    else:
        return a / b

##
# @brief function that computes absolute value of a number
# @param a number to be made absolute
# @return absolute value of parameter a
def abs(a):
    return a if a > 0 else a * -1

##
# @brief function that calculates root of a number
# @param a number we want to calculate root of
# @param b optional parameter, dimension of root, default is 2
# @raises ValueError if param a is lower than 0
# @return b-dimensional root of number given in param a
def sqrt(a, b=2):
    if b % 2 == 0:
        if a >= 0:
            return float(a ** (1 / b))
        else:
            raise ValueError
    else:
        return -float(abs(a) ** (1 / b)) if a <0 else float(abs(a) ** (1 / b))

##
# @brief function that calculates factorial of a given number
# @param a number we want to calculate factorial of
# @raises ValueError if param a is lower than 0 or if it there is a non-decimal part
# @return factorial of number in param a
def fact(a):
    if a < 0 or a % 1 != 0:
        raise ValueError
    else:
        num = 1
        while a >= 1:
            num = num * a
            a = a - 1
        return num

##
# @brief function that multiplies number to given power(exponent)
# @param a number we want to multiply
# @param b optional parametr, exponent, defaultly = 2
# @raises ValueError if both of the arguments are equal to 0
# @return result of a to the power of b in form of a float
def pow(a, b=2):
	if a == 0 and b == 0:
		raise ValueError
	else:
		return float(a ** b)

##
# @brief Function that calculates standard deviation. It reads numbers from standard input.
# @return standard deviation of numbers in input
def stdev():
    list2 = input()
    list2= sorted(list2.split(" "))
    N = len(list2)
    par = N - 1
    frequency_distribution = {i:0 for i in list2}
    for x in list2:
        frequency_distribution[x] =+ 1
    cumulative_sum = 0
    for i in list2:
        cumulative_sum += frequency_distribution[i]
        if cumulative_sum > int(len(list2)*0.5):
            mid = i
            break
    res = 0
    for i in list2:
        tmp = (int(i) - int(mid)) ** 2
        res = res + tmp
    s = res / par
    return sqrt(s)