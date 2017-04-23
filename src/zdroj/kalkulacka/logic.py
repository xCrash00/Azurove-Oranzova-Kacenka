#!/usr/bin/env python3

##
# @file logic.py
# File containing definitions of functions called by calculator.
#

from kalkulacka import math_lib

##
# @brief global variable containing input from user to be calculated
# functions in this file work with and modify the content of this variable
global term
term = ""
##
# @brief global variable in which the result of term will be stored
global res
res = 0

##
# @brief Function that adds given number to global string "term".
# @param num: Number to be appended.
# @return 0 if everything goes well
def num_pressed(num):
    global term
    term += str(num)
    return 0

##
# @brief Function that adds given operator to global string "term", surrounded by two spaces, so the string can be
# parsed later.
# @param operator: Operator to be appended. (+,-,*,/,^)
# @return 0 if everything goes well
def operator_pressed(operator):

    global term
    term += ' ' + operator + ' '
    return 0

##
# @brief Function that adds factorial symbol to global string "term". There will be a space before '!'.
# @return 0 if everything goes well
def fact_pressed():

    global term
    term += ' !'
    return 0

##
# @brief Function that adds ' abs' string to global string "term". There will be a space before 'abs'.
# @return 0 if everything goes well
def abs_pressed():

    global term
    term += ' abs'
    return 0

##
# @brief Function that adds root symbol to global string "term". Root symbol √ will be surrounded by spaces.
# @return 0 if everything goes well
def sqrt_pressed():

    global term
    term += ' √ '
    return 0

##
# @brief Function that adds minus symbol to global string "term". Minus sign will stick to number, because there are
# no spaces around '-'.
# @return 0 if everything goes well
def negate_pressed():

    global term
    if len(term) > 0:
        if term[-1] == '-':
            term = term[:-1]
        else:
            term += '-'
    else:
        term += '-'
    return 0

##
# @brief Function that clears global term by setting it equal to ''. It sets global res to 0.
# @return 0 if everything goes well
def c_pressed():

    global term
    term = ''
    global res
    res = 0
    return 0

##
# @brief Function that removes last given sequence from global term. It removes a single operator, or continuous
# numbers, or Error from term.
# @return 0 if everything goes well
def ce_pressed():

    global term
    operators = ['+', '-', '*', '/', '√', '!', 'abs', '^', ')', '(']
    numbers = ['1','2','3','4','5','6','7','8','9','0','.']
    length = len(term)
    if length == 0:
        return 0
    if term == 'Error':
        term = ''
        return 0
    if term[-1] == ' ':
        term = term[:-1]
    if term[-1] in operators:
        term = term[:-2]
    elif term[-1] in numbers:
        while term[-1] in numbers:
            if len(term) == 1:
                if term[-1] in numbers:
                    term = ''
                    return 0
                else:
                    return 0
            term = term[:-1]



    """
    if len(term) == 0:  # if there is nothing in term, result is 0
        return 0
    if term[-1] == ' ':  #if the string ends with space, remove it
        term = term[:-1]
    while term[-1] != ' ':  # as long as the last char isnt space, remove it
        if len(term) == 1:  #if we have encountered the first char, set term empty
            term = ''
            return 0
        term = term[:-1]
    if term[-1] == ' ':  #if there still is a space, remove it
        term = term[:-1]
    return 0
    """

##
# @brief Function that adds opening parenthesis symbol to global string "term". There will be a space after it.
# @return 0 if everything goes well
def leftpar_pressed():

    global term
    term += '( '
    return 0

##
# @brief Function that adds closing parenthesis symbol to global string "term". There will be a space after it.
# @return 0 if everything goes well
def rightpar_pressed():
    global term
    term += ' )'
    return 0

##
# @brief Function that splits string in global term at each space and appends these parts to a list.
# @return parts list of elements, that were separated by spaces in global term
def parse():

    parts = []
    for item in term.split(' '):
        parts.append(item)
    return parts

##
# @brief Function that adds opening parenthesis symbol to global string "term". There will be a space after it.
# @param list list, which we want to check for mathematical validity
# @raises ValueError if param list is not valid
# @return 0 if everything goes well, sets term equal to Error and raises ValueError if not
def is_valid(list):

    operators = ['+', '-', '*', '/', '√', '!', 'abs', '^']  #list of possible operators
    global term
    index = -1
    for item in list:  # iterate over items in list
        index += 1  # manualy increase index
        if index + 1 <= len(list):  # check, if we can look one item further
            if is_number(item):  #there must be an operator after each number, unless it is end of string
                if index + 1 != len(list):
                    if list[index + 1] not in operators:  #if there isnt an operator
                        term = 'Error'
                        raise ValueError
            elif item in operators:  # there must be a number after each operator, except for fact and abs
                if item not in ['!', 'abs']:
                    if is_number(list[index + 1]) == False:
                        term = 'Error'
                        raise ValueError
        elif item == '':  #parse function will leave this as last item of a list, if there was no number after operator
            term = 'Error'
            raise ValueError
    return 0

##
# @brief Checks, if there are valid parentheses combinations in string.
# @param src list in which we want to check parentheses
# @raises ValueError when the parentheses are written in wrong way
# @return d dictionary containing tuples of two numbers. First number is index of opening parentheses, the other one
# is index of closing parentheses.
def find_matching_par(src):

    istart = []  # stack of indices of opening parentheses
    d = {}
    global term
    for i, c in enumerate(src):
        if c == '(':
            istart.append(i)
        if c == ')':
            try:
                d[istart.pop()] = i
            except IndexError:
                term = 'Too many closing parentheses'
                raise ValueError
    if istart:  # check if stack is empty afterwards
        term = 'Too many opening parentheses'
        raise ValueError
    return d

##
# @brief Main function for evaluating the string in term. Recursively removes parenthesis and evaluates string in term.
# @param source list of items to evaluate
# @warning might crash the program on unexpected input
# @raises ValueError if there was ValueError raised during the process
# @return simplest[0] first item in a final string, which in the last phase contains only the result.
def get_res(source):

    for item in source:
        if item not in [' ', '', '!', 'abs', '√', '*', '/', '^', '+', '-', '(', ')']:
            if not is_number(item):
                raise ValueError
    if len(source) == 1:
        return source[0]
    try:
        find_matching_par(source)
    except ValueError:
        raise ValueError
    par = sorted(list(find_matching_par(source).items()))

    if par == []:
        try:
            is_valid(source)
        except ValueError:
            raise ValueError
        op_highprio = ['!', 'abs', '√']
        op_prio = ['*', '/', '^']
        op = ['+', '-']

        simpler = []
        skip = False
        index = -1
        index2 = -1
        for item in source:
            if skip == True:
                skip = False
                continue
            simpler.append(item)
            index += 1
            index2 += 1
            if item in op_highprio:
                #index = simpler.index(item)
                if item == '!':
                    value = simpler[index - 1]
                    simpler[index - 1] = math_lib.fact(float(value))
                    del simpler[index]
                    index -= 1
                    print(simpler)
                elif item == 'abs':
                    value = simpler[index - 1]
                    simpler[index - 1] = math_lib.abs(float(value))
                    del simpler[index]
                    index -= 1
                    print(simpler)
                else:
                    value1 = source[index + 1]
                    if simpler[index - 1] == '':
                        simpler = simpler[:-2]
                        simpler.append(math_lib.sqrt(float(value1)))
                    else:
                        value2 = simpler[index2 - 1]
                        simpler = simpler[:-2]
                        simpler.append(math_lib.sqrt(float(value1), float(value2)))
                    print(simpler)
                    skip = True
        simplerer = []
        skip = False
        index = -1
        index2 = -1
        for item in simpler:
            index += 1
            if skip == True:
                skip = False
                continue
            simplerer.append(item)
            print(simplerer)

            index2 += 1
            if item in op_prio:
                value1 = simplerer[index2 - 1]
                value2 = simpler[index + 1]
                simplerer = simplerer[:-2]
                index2 -= 1
                print(simplerer)
                print(index)
                print(index2)
                if item == '*':
                    simplerer.append(math_lib.mul(float(value1), float(value2)))
                    print(simplerer)
                    skip = True
                elif item == '^':
                    simplerer.append(math_lib.pow(float(value1), float(value2)))
                    print(simplerer)
                    skip = True
                else:
                    simplerer.append(math_lib.div(float(value1), float(value2)))
                    print(simplerer)
                    skip = True
        simplest = []
        skip1 = False
        index = -1
        index2 = -1
        for item in simplerer:
            index += 1
            if skip1 == True:
                skip1 = False
                continue
            simplest.append(item)
            index2 += 1
            if item in op:
                value1 = simplest[index2 - 1]
                value2 = simplerer[index + 1]
                simplest = simplest[:-2]
                index2 -= 1
                if item == '+':
                    simplest.append(math_lib.add(float(value1), float(value2)))
                    print(simplest)
                    skip1 = True
                elif item == '-':
                    simplest.append(math_lib.sub(float(value1), float(value2)))
                    print(simplest)
                    skip1 = True
        return simplest[0]
    else:
        first = par[0]
        num1 = first[0] + 1
        num2 = first[1]
        try:
            get_res(source[num1:num2])
            source[first[0]] = get_res(source[num1:num2])
        except ValueError:
            raise ValueError
        for a in range(num1, num2 + 1):
            del source[num1]
        try:
            get_res(source)
            return get_res(source)
        except ValueError:
            raise ValueError

##
# @brief Function that checks, if there is a number in argument.
# @param s string to check
# @return True if s is a number, False otherwise
def is_number(s):

    try:
        float(s)
        return True
    except ValueError:
        return False

##
# @brief Function that is called by pressing = in calculator. It calls the parsing function and gives its output to
# get_res as an argument. It puts the result to global res and returns it in proper format. It sets 1.0 to 1. and
# if there is only a number in term, it becomes the result. It also checks for errors.
# @raises ValueError if there was a ValueError in get_res
# @return res - overwriten global res, containing the result of string in global term
def result():

    global res
    global term
    source = parse()
    if is_number(term):
        res = float(term)
        if res.is_integer():
            res = int(res)
        '''res = term
        if '.' in term:
            res = math_lib.add(float(res), float(0))
            print(res)
            if float(res) + 5 == 5:
                res = 0'''
        return res
    elif term == '':
        res = 0
        return res
    else:
        try:
            get_res(source)
            res = get_res(source)
        except ValueError:
            term = 'Error'
            return res
    if is_number(res):
        res = float(res)
        if res.is_integer():
            res = int(res)
    return res

def del_num(    ):
    global term
    operators = ['+', '-', '*', '/', '√', '!', 'abs', '^', ')', '(']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    length = len(term)
    if length == 0:
        return 0
    if term == 'Error':
        term = ''
        return 0
    if term[-1] == ' ':
        term = term[:-1]
    if term[-1] in operators:
        term = term[:-2]
    elif term[-1] in numbers:
        term = term[:-1]


def cut_res():
    global res
    res = str(res)
    velikostokna = 17
    lenght = len(res)
    print(lenght)
    dotind = -1
    if '.' in str(res):
        dotind = res.index('.')
    if lenght > velikostokna and dotind != -1:
        if dotind < velikostokna:
            res = str(res)[0:velikostokna]
            lenght = len(res)
    if lenght > velikostokna:
        num=0
        first=str(res)[0]
        num = lenght - 1
        if num < 10:
            new = first + '.' + str(res)[1:velikostokna - 4] + 'e+' + str(num)
        elif num < 100:
            new = first + '.' + str(res)[1:velikostokna - 5] + 'e+' + str(num)
        else:
            new = first + '.' + str(res)[1:velikostokna - 6] + 'e+' + str(num)
        res = new
        return res

