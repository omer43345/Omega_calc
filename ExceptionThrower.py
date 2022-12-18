validation_error_message_dict = {
    'unknown_char': 'equation can only contain numbers, operators and brackets, unknown char found at index',
    'empty': 'you must enter an equation that contains at least one number',
    'brackets': 'you have invalid bracket in the equation at index',
    'operator': 'expect for operand after the operator in index',
    'right': 'expect for operator that get 2 operands after the operand in index',
    'operand': 'expect for operator in index after the operand in index'}
arithmetic_error_message_dict = {
    'division_by_zero': 'you can not divide by zero',
    'factorial': 'you can do factorial only on positive and natural numbers',
    'digit_sum': 'you can not do digit sum on really big or small numbers',
    'complex_number': 'the result of power can not be a complex number',
    'number_too_big_or_small': 'the system can not calculate numbers too big or small'}
exit_error_message = {'EOF': 'EOF error occurred, closing the program...',
                      'KeyboardInterrupt': 'KeyboardInterrupt ,closing the program...'}


def create_error_message(reason: str, index: int) -> str:
    """
    This function get the reason of the exception and return the error message of the reason from the right dict
    :param index: the index of the problem in the equation
    :param reason: the reason of the exception
    :return: the error message of the reason from the right dict
    """
    if reason in validation_error_message_dict:
        return 'ValueError-> ' + validation_error_message_dict[reason] + ' ' + str(index)
    if reason in arithmetic_error_message_dict:
        return 'ArithmeticError-> ' + arithmetic_error_message_dict[reason]
    return 'SystemExit-> ' + exit_error_message[reason]


def throw_exception(reason: str, index: int = -1, exit_program: bool = False):
    """
    This function raise an exception with the error message of the reason
    :param reason: the reason of the exception
    :param index: the index of the problem in the equation
    :param exit_program: if the program should exit after the exception
    :return:
    """
    error_message = create_error_message(reason, index)
    if exit_program:
        print(error_message)
        exit()
    raise Exception(error_message)
