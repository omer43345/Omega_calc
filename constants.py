from ExceptionThrower import throw_exception

"""
This section of the file contains all the functions that are used in the calculator
"""


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
    if num < 1 or num % 1 != 0:
        throw_exception('factorial')
    for i in range(1, int(num)):
        num *= i
    return num


def digits_sum(num):
    if 'e' in str(num) or 'inf' == str(num):
        throw_exception('digit_sum')
    res = 0
    for digit in str(num):
        if digit not in ['.', '-']:
            res += int(digit)
    if num < 0:
        res *= -1
    return res


def is_number(token: str) -> bool:
    """
    This function check if the token is a number
    :param token: the token to check
    :return: True if the token is a number, False otherwise
    """
    try:
        float(token)
        return True
    except ValueError:
        return False


"""
This section of the file contains all the constants that are used in the calculator"""
priority_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6, '#': 6}
operators_dict = {'+': plus, '-': minus, '*': multiply, '/': divide, '^': power, '%': mod, '$': maximum, '&': minimum,
                  '@': avg, '~': neg, '!': factorial, '#': digits_sum}
side_of_operands = {'+': 'both', '-': 'both', '*': 'both', '/': 'both', '^': 'both', '%': 'both', '$': 'both',
                    '&': 'both', '@': 'both', '~': 'right', '!': 'left', '#': 'left'}
what_should_come_next = {'operand': 'left.both.cl_bracket', 'both': 'operand.right.op_bracket',
                         'right': 'operand', 'left': 'left.both.cl_bracket'}
operators_that_changing_sign = ['+', '-']
