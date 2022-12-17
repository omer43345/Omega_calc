from constants import *

error_message_dict = {
    'unknown_char': 'equation can only contain numbers, operators and brackets, unknown char found at index',
    'empty': 'you must enter an equation that contains at least one number',
    'extra_token': 'you have entered an extra token in the end of the equation',
    'brackets': 'you have invalid brackets in the equation',
    'operator': 'expect for operand in index',
    'right': 'expect for operator that get 2 operands in index',
    'operand': 'expect for operator in index',
    'factorial': 'you can do factorial only on positive and natural numbers',
    'division_by_zero': 'you can not divide by zero',
    'digit_sum': 'you can not do digit sum on really big or small numbers',
    'EOF': 'EOF error occurred, closing the program...',
    'KeyboardInterrupt': 'KeyboardInterrupt ,closing the program...',
    'complex_number': 'the result of power can not be a complex number',
    'number_too_big_or_small': 'the system can not calculate numbers too big or small', }


def create_error_message(reason: str):
    # return the error message of the reason by the error_message_dict
    return error_message_dict.get(reason)


def throw_exception(reason: str, index: int = -1, exit_program: bool = False):
    """
    This function raise an exception with the error message of the reason from the error_message_dict
    :param reason: the reason of the exception
    :param index: the index of the problem in the equation
    :param exit_program: if the program should exit after the exception
    :return:
    """
    error_message = create_error_message(reason)
    if index != -1:
        error_message += ' ' + str(index)
    if exit_program:
        print(error_message)
        exit()
    raise Exception(error_message)
