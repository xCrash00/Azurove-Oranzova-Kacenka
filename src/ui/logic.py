#!/usr/bin/env python3

from src import math_lib

global term
term = ""

def num_pressed(num):
	global term
	term += str(num)
	print(term)
	return 0


def operator_pressed(operator):
	global term
	term += ' ' + operator + ' '
	print(term)
	return 0


def fact_pressed():
	global term
	term += ' !'
	print(term)
	return 0


def abs_pressed():
	global term
	term += ' abs'
	print(term)
	return 0


def sqrt_pressed():
	global term
	term += ' sqrt'
	print(term)
	return 0


def negate_pressed():
	global term
	term += '-'
	print(term)
	return 0

def c_pressed():
	global term
	term = ''
	return 0


'''
maze jen posledni cislo za operatorem, neumi zatim smazat operator
'''

def ce_pressed():
	global term
	while term[-1] != ' ':
		term = term[:-1]
	return 0


def parse():
	parts = []
	for item in term.split(' '):
		parts.append(item)
	return parts


def get_res():
	op_highprio = ['!', 'abs', 'sqrt']
	op_prio = ['*', '/']
	op = ['+', '-']
	list = parse()
	print(list)
	simpler = []
	for item in list:
		simpler.append(item)
		if item in op_highprio:
			index = simpler.index(item)
			value = simpler[index - 1]
			if item == '!':
				simpler[index - 1] = math_lib.fact(float(value))
				del simpler[index]
				print(simpler)
			elif item == 'abs':
				simpler[index - 1] = math_lib.abs(float(value))
				del simpler[index]
				print(simpler)
			else:
				simpler[index - 1] = math_lib.sqrt(float(value))
				del simpler[index]
				print(simpler)
	simplerer = []
	print(simpler)
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
			else:
				simplerer.append(math_lib.div(float(value1), float(value2)))
				print(simplerer)
				skip = True
	simplest = []
	print(simplerer)
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
	return simplest
