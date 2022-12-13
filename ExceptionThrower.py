from constants import *

error_message_dict = {
    'unknown_char': 'equation can only contain numbers, operators and brackets, unknown char found at index',
    'empty': 'you must enter an equation that contains at least one number',
    'extra_token': 'you have entered an extra token in the end of the equation',
    'brackets': 'you have entered an invalid number of brackets',
    'operator': 'expect for operand in index',
    'operand': 'expect for operator in index',
    'factorial': 'you can do factorial only on positive and natural numbers',
    'division_by_zero': 'you can not divide by zero'}


def create_error_message(reason: str):
    return error_message_dict.get(reason)


def throw_exception(reason: str, index: int = -1):
    if index != -1:
        print(create_error_message(reason) + ' ' + str(index))
    else:
        print(create_error_message(reason))
    restart()


def restart():
    from main import start
    start()
