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


def pow_pressed():
    global term
    term += ' Pow '
    return 0

def abs_pressed():
    global term
    term += ' abs'
    return 0


def sqrt_pressed():
    global term
    term += 'sqrt '
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
    term += ','
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
    if istart:  # check if stack is empty afterwards
        term = 'Too many opening parentheses'
    return d


def get_res(source):
    par = sorted(list(find_matching_par(source).items()))
    if par == []:
        op_highprio = ['!', 'abs', 'sqrt']
        op_prio = ['*', '/', 'Pow']
        op = ['+', '-']

        simpler = []
        for item in source:
            skip1 = False
            skip2 = False
            if skip1 == True:
                skip1 = False
                continue
            if skip2 == True:
                skip2 == False
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
                    index = source.index(item)
                    value = source[index + 1]
                    value2 = 2
                    index = simpler.index(item)
                    if ',' in value:
                        value2 = value.split(',')[1]
                        value = value.split(',')[0]
                    simpler[index] = math_lib.sqrt(float(value), float(value2))
                    skip = True
                    print(simpler)
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
        skip = False
        for item in simplerer:
            if skip == True:
                skip = False
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
                    skip = True
                elif item == '-':
                    simplest.append(math_lib.sub(float(value1), float(value2)))
                    print(simplest)
                    skip = True
        return simplest[0]
    else:
        first = par[0]
        num1 = first[0] + 1
        num2 = first[1]
        source[first[0]] = get_res(source[num1:num2])
        for a in range(num1, num2 + 1):
            del source[num1]
        return get_res(source)


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
        res = get_res(source)
    if res.is_integer():
        res = int(res)
    return res
