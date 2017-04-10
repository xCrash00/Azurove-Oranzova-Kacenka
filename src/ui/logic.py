#!/usr/bin/env python3

from src import math_lib

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


def c_pressed():
	global term
	term = ''
	return 0


def ce_pressed():
	global term
	while (term[-1] != ' '):
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
	list = parse()
	print(list)
	simpler = []
	for item in list:
		simpler.append(item)
		if item in op_highprio:
			index = simpler.index(item)
			value = simpler[index - 1]
			if item == '!':
				simpler[index - 1] = math_lib.fact(int(value))
				del simpler[index]
				print(simpler)
			elif item == 'abs':
				simpler[index - 1] = math_lib.abs(int(value))
				print(simpler)
				del simpler[index]
			else:
				simpler[index - 1] = math_lib.sqrt(int(value))
				del simpler[index]
				print(simpler)
	simplerer = []
	for item in simpler:
		simplerer.append(item)
		if item in op_prio:
			index = simplerer.index(item)
			value1 = simplerer[index - 1]
			value2 = simplerer[index + 1]
			if item == '*':
				simplerer[index - 1] = math_lib.mul(value1, value2)
				print(simplerer)
				del simplerer[index]
				del simplerer[index + 1]
			else:
				simplerer[index - 1] = math_lib.div(value1, value2)
				print(simplerer)
				del simplerer[index]
				del simplerer[index + 1]

	return simplerer


num_pressed('-')
num_pressed(1)
num_pressed(0)
abs_pressed()
fact_pressed()
sqrt_pressed()
operator_pressed('*')
num_pressed(2)
get_res()
