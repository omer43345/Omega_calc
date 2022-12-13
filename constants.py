from ExceptionThrower import *


def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        throw_exception('division_by_zero')
    return num1 / num2


def power(num1, num2):
    return pow(num1, num2)


def mod(num1, num2):
    if num2 == 0:
        throw_exception('division_by_zero')
    return num1 % num2


def minimum(num1, num2):
    if num1 < num2:
        return num1
    return num2


def maximum(num1, num2):
    if num1 > num2:
        return num1
    return num2


def neg(num):
    return -num


def avg(num1, num2):
    return (num1 + num2) / 2


def factorial(num):
    if num < 1 or '.' not in str(num):
        throw_exception('factorial')
    if num == 1:
        return 1
    return num * factorial(num - 1)


def digits_sum(num):
    res = 0
    for digit in str(num):
        if digit not in ['.', '-']:
            res += int(digit)
    if num < 0:
        res *= -1
    return res


def is_number(token: str) -> bool:
    try:
        float(token)
        return True
    except ValueError:
        return False


priority_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6, '#': 6}
operators_dict = {'+': plus, '-': minus, '*': multiply, '/': divide, '^': power, '%': mod, '$': maximum, '&': minimum,
                  '@': avg, '~': neg, '!': factorial, '#': digits_sum}
side_of_operands = {'+': 'both', '-': 'both', '*': 'both', '/': 'both', '^': 'both', '%': 'both', '$': 'both',
                    '&': 'both', '@': 'both', '~': 'right', '!': 'left', '#': 'left'}
what_should_come_next = {'operand': 'left.both.cl_bracket', 'both': 'operand.right.op_bracket',
                         'right': 'operand', 'left': 'left.both.cl_bracket'}
operators_that_changing_sign = ['+', '-']
