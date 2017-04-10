#!/usr/bin/env python3

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        raise ValueError
    else:
        return a / b

def abs(a):
    return a if a > 0 else a * -1

def sqrt(a, b=2):
    if b % 2 == 0:
        if a >= 0:
            return float(a ** (1 / b))
        else:
            raise ValueError
    else:
        return -float(abs(a) ** (1 / b)) if a <0 else float(abs(a) ** (1 / b))

def fact(a):
    if a < 0 or a % 1 != 0:
        raise ValueError
    else:
        num = 1
        while a >= 1:
            num = num * a
            a = a - 1
        return num

def pow(a, b=2):
	if a == 0 and b == 0:
        raise ValueError
    else:
        return float(a ** b)
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


