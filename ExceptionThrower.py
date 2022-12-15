from constants import *

error_message_dict = {
    'unknown_char': 'equation can only contain numbers, operators and brackets, unknown char found at index',
    'empty': 'you must enter an equation that contains at least one number',
    'extra_token': 'you have entered an extra token in the end of the equation',
    'brackets': 'you have entered an invalid number of brackets',
    'operator': 'expect for operand in index',
    'right': 'expect for operator that get 2 operands in index',
    'operand': 'expect for operator in index',
    'factorial': 'you can do factorial only on positive and natural numbers',
    'division_by_zero': 'you can not divide by zero',
    'digit_sum': 'you can not do digit sum on really big numbers',
    'EOF': 'you have entered an EOF, program closed',
    'KeyboardInterrupt': 'you have entered a Keyboard Interrupt, program closed',
    'complex_number': 'the result of power can not be a complex number'}


def create_error_message(reason: str):
    # return the error message of the reason by the error_message_dict
    return error_message_dict.get(reason)


def throw_exception(reason: str, index: int = -1, exit_program: bool = False):
    """
    This function let the user know what is the problem with the equation and restart the program if needed
    :param reason: the reason of the exception
    :param index: the index of the problem in the equation
    :param exit_program: if the program should exit after the exception
    :return:
    """
    if index != -1:
        print(create_error_message(reason) + ' ' + str(index))
    else:
        print(create_error_message(reason))
    if exit_program:
        exit()
    restart()


def restart():
    # restart the program
    from main import start
    start()
