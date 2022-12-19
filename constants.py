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
    if num1 == 0 and num2 == 0:
        throw_exception('division_by_zero')
    try:
        num1 = pow(num1, num2)
    except OverflowError:
        throw_exception('number_too_big_or_small')
    if type(num1) == complex:
        throw_exception('complex_number')
    return num1


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
        if str(num) == 'inf':
            throw_exception('number_too_big_or_small')
    return num


def digits_sum(num):
    res = sum(int(digit) for digit in str(num) if digit.isdigit())
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
operators_functions_dict = {'+': plus, '-': minus, '*': multiply, '/': divide, '^': power, '%': mod, '$': maximum,
                            '&': minimum, '@': avg, '~': neg, '!': factorial, '#': digits_sum}
side_of_operands = {'+': 'both', '-': 'both', '*': 'both', '/': 'both', '^': 'both', '%': 'both', '$': 'both',
                    '&': 'both', '@': 'both', '~': 'right', '!': 'left', '#': 'left'}
what_should_come_next = {'operand': 'left.both.cl_bracket', 'both': 'operand.right.op_bracket.unary_minus',
                         'right': 'operand.unary_minus', 'left': 'left.both.cl_bracket'}
operators_that_changing_sign = ['+', '-']
operators_names_dict = {'+': 'plus', '-': 'minus', '*': 'multiply', '/': 'divide', '^': 'power', '%': 'mod',
                        '$': 'maximum', '&': 'minimum', '@': 'avg', '~': 'neg', '!': 'factorial', '#': 'digits_sum'}
WELCOME_MESSAGE = f'\nWelcome to the omega calculator, in this calculator you can do the following operations:\n {operators_names_dict} \n You can also use brackets, spaces and unary minuses in your equation  \n'
