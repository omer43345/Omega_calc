"""
This file contains all the error messages of the program in different dicts by the reason of the exception,
this file also contains the function that create the error message of the reason and the function that throw the exception
"""

validation_error_message_dict = {
    'unknown_char': 'equation can only contain numbers, operators and brackets, the char "%s" that in index %d is not a valid char',
    'operator': 'you can put the %s that in index %d only after a number or an operator that have operand before it',
    'right': 'you can put the %s that in index %d only after operator that get two operands or unary minus',
    'operand': 'you can put the %s that in index %d only after operator that get two operands or operator that have operand after it'}
brackets_error_message_dict = {'not_closed': 'in index %d you have unclosed bracket',
                               'not_opened': 'in index %d you have unopened bracket'}
start_and_end_error_message_dict = {'start': 'the equation can not start with %s',
                                    'end': 'the equation can not end with %s'}
arithmetic_error_message_dict = {
    'division_by_zero': 'you can not divide by zero',
    'factorial': 'you can do factorial only on positive and natural numbers',
    'digit_sum': 'you can not do digit sum on really big or small numbers',
    'complex_number': 'the result of power can not be a complex number',
    'number_too_big_or_small': 'the system can not calculate numbers too big or small'}
exit_error_message = {'EOF': 'EOF error occurred, closing the program...',
                      'KeyboardInterrupt': 'KeyboardInterrupt ,closing the program...'}
empty_equation = {'empty': 'you must enter an equation that contains at least one number'}


def create_error_message(reason: str, index: int, token: str) -> str:
    """
    This function get the reason of the exception and return the error message of the reason from the right dict
    :param token: the token that cause the exception
    :param index: the index of the problem in the equation
    :param reason: the reason of the exception
    :return: the error message of the reason from the right dict
    """
    if reason in start_and_end_error_message_dict:
        return 'ValueError-> ' + start_and_end_error_message_dict.get(reason) % token
    if reason in validation_error_message_dict:
        return 'ValueError-> ' + validation_error_message_dict.get(reason) % (token, index)
    if reason in arithmetic_error_message_dict:
        return 'ArithmeticError-> ' + arithmetic_error_message_dict[reason]
    if reason in brackets_error_message_dict:
        return 'ValueError-> ' + brackets_error_message_dict[reason] % index
    if reason in empty_equation:
        return 'ValueError-> ' + empty_equation[reason]
    return 'SystemExit-> ' + exit_error_message[reason]


def throw_exception(reason: str, token: str = '', index: int = -1, exit_program: bool = False):
    """
    This function raise an exception with the error message of the reason
    :param token: the token that cause the exception
    :param reason: the reason of the exception
    :param index: the index of the problem in the equation
    :param exit_program: if the program should exit after the exception
    :return:
    """
    error_message = create_error_message(reason, index, token)
    if exit_program:
        print(error_message)
        exit()
    raise Exception(error_message)
