#!/usr/bin/env python3

from src import math_lib

global term
term = ""
global res
res = 0

def num_pressed(num):
    global term
    term += str(num)
    return 0


def operator_pressed(operator):
    global term
    term += ' ' + operator + ' '
    return 0

def fact_pressed():
    global term
    term += ' !'
    return 0

def abs_pressed():
    global term
    term += ' abs'
    return 0


def sqrt_pressed():
    global term
    term += ' √ '
    return 0


def negate_pressed():
    global term
    term += '-'
    return 0


def c_pressed():
    global term
    term = ''
    global res
    res = 0
    return 0


def ce_pressed():
    global term
    if len(term) == 0:
        return 0
    if term[-1] == ' ':
        term = term[:-1]
    while term[-1] != ' ':
        if len(term) == 1:
            term = ''
            return 0
        term = term[:-1]
    if term[-1] == ' ':
        term = term[:-1]
    return 0


def comma_pressed():
    global term
    term += ' , '
    return 0


def leftpar_pressed():
    global term
    term += '( '
    return 0


def rightpar_pressed():
    global term
    term += ' )'
    return 0

def parse():
    parts = []
    for item in term.split(' '):
        parts.append(item)
    return parts


def is_valid(list):
    operators = ['+', '-', '*', '/', '√', 'fact']
    global term
    index = -1
    for item in list:
        index += 1
        if index + 1 <= len(list):
            if is_number(item):
                if index + 1 != len(list):
                    if list[index + 1] not in operators:
                        term = 'Error'
                        raise ValueError
            elif item in operators:
                if is_number(list[index + 1]) == False:
                    term = 'Error'
                    raise ValueError
        elif item == '':
            term = 'Error'
            raise ValueError
    return 0

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


def get_res(source):
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
        op_prio = ['*', '/', 'Pow']
        op = ['+', '-']

        simpler = []
        skip = False
        for item in source:
            if skip == True:
                skip = False
                continue
            simpler.append(item)
            if item in op_highprio:
                index = simpler.index(item)
                if item == '!':
                    value = simpler[index - 1]
                    simpler[index - 1] = math_lib.fact(float(value))
                    del simpler[index]
                    print(simpler)
                elif item == 'abs':
                    value = simpler[index - 1]
                    simpler[index - 1] = math_lib.abs(float(value))
                    del simpler[index]
                    print(simpler)
                else:
                    index = simpler.index(item)
                    index2 = source.index(item)
                    value1 = source[index + 1]
                    print(index)
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
        for item in simpler:
            if skip == True:
                skip = False
                continue
            simplerer.append(item)
            if item in op_prio:
                index = simpler.index(item)
                index2 = simplerer.index(item)
                value1 = simplerer[index2 - 1]
                value2 = simpler[index + 1]
                simplerer = simplerer[:-2]
                if item == '*':
                    simplerer.append(math_lib.mul(float(value1), float(value2)))
                    print(simplerer)
                    skip = True
                elif item == 'Pow':
                    simplerer.append(math_lib.pow(float(value1), float(value2)))
                    print(simplerer)
                    skip = True
                else:
                    simplerer.append(math_lib.div(float(value1), float(value2)))
                    print(simplerer)
                    skip = True
        simplest = []
        skip1 = False
        for item in simplerer:
            if skip1 == True:
                skip1 = False
                continue
            simplest.append(item)
            if item in op:
                ind = simplerer.index(item)
                ind2 = simplest.index(item)
                value1 = simplest[ind2 - 1]
                value2 = simplerer[ind + 1]
                simplest = simplest[:-2]
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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def result():
    global res
    global term
    source = parse()
    if is_number(term):
        res = float(term)
    elif term == '':
        return res
    else:
        try:
            get_res(source)
            res = get_res(source)
        except ValueError:
            term = 'Error'
            return res
    if res.is_integer():
        res = int(res)
    return res
