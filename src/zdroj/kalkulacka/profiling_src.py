import math_lib
import random
import cProfile
##
# @brief Function that calculates standard deviation. It reads numbers from standard input.
# @return standard deviation of numbers in input
def stdev():
    list2 = input()
    list2 = sorted(list2.split(","))
    N = len(list2)
    par = math_lib.sub(N,1)
    num = 0
    for i in list2:
        num = math_lib.add(num,int(i))
    num2 = math_lib.div(num,N)
    res = 0
    for i in list2:
        tmp = math_lib.pow(math_lib.sub(int(i),num2))
        res = math_lib.add(res,tmp)
    s = math_lib.div(res,par)
    return math_lib.sqrt(s)

input1 = random.sample(range(5000),10)
input2 = random.sample(range(5000),100)
input3 = random.sample(range(5000),1000)