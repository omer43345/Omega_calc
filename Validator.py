from constants import *
from ExceptionThrower import throw_exception


def validate(token_list: list):
    """
    This function get token list and validate it
    :param token_list: token list
    :return:
    """
    char_validation(token_list)
    check_brackets(token_list)
    token_list_validator(token_list)


def char_validation(token_list: list):
    """
    This function get token list and check if there is a char that is not a valid char
    :param token_list: token list
    :return:
    """
    for token in token_list:
        if not (is_number(token) or operators_functions_dict.get(token) or token in ['(', ')']):
            throw_exception('unknown_char', token, token_list.index(token))


def check_brackets(token_list: list):
    """
    This function get token list and check if there is a problem with brackets
    :param token_list: token list
    :return:
    """
    index = 0
    while index < len(token_list):
        if token_list[index] == '(':
            index = check_bracket_and_get_cl_bracket_index(token_list, index + 1)
            index -= 1
        elif token_list[index] == ')':
            throw_exception('not_opened', ')', index)
        index += 1


def check_bracket_and_get_cl_bracket_index(token_list: list, index: int) -> int:
    """
    This function get token list and index and check if there is a problem the bracket that start in index
    :param token_list: token list
    :param index: index of the bracket
    :return: index of the closing bracket
    """
    num_of_brackets = 1
    index_of_op_bracket = index - 1
    while index < len(token_list) and num_of_brackets > 0:
        if token_list[index] == '(':
            index_of_op_bracket = index
            num_of_brackets += 1
        elif token_list[index] == ')':
            num_of_brackets -= 1
        index += 1
    if num_of_brackets == 0:
        return index
    throw_exception('not_closed', '(', index_of_op_bracket)


def token_list_validator(token_list: list):
    """
    This function get token list and check if there is a problem with the token list by checking what should come next after each token
    :param token_list: token list
    :return:
    """
    next_item = what_should_come_next.get('both')
    index = 0
    if not token_list:
        throw_exception('empty')
    for token in token_list:
        list_next = next_item.split('.')
        if not is_token_valid(list_next, token):
            if index == 0:
                throw_exception('start', token)
            throw_exception(get_reason(token), token, index)
        if side_of_operands.get(token) == 'right':
            check_right_operators(token_list, index + 1)
        next_item = get_next(token)
        index += 1
    if what_should_come_next.get('operand') != next_item:
        throw_exception('end', token_list[-1])


def get_reason(token: str) -> str:
    """
    This function get token and return the reason of the error
    :param token: token
    :return: reason of the error
    """
    if side_of_operands.get(token) == 'right':
        return 'right'
    if token in side_of_operands.keys() or token == ')':
        return 'operator'
    if is_number(token) or token == '(':
        return 'operand'


def is_token_valid(list_next: list, token: str) -> bool:
    """
    This function get list of what should come next and token and check if the token is valid
    :param list_next: list of what should come next
    :param token: token
    :return: True if the token is valid, False otherwise
    """
    for item in list_next:
        if item == 'unary_minus' and token == '-':
            return True
        if item == side_of_operands.get(token):
            return True
        if item == 'operand' and (is_number(token) or token == '('):
            return True
        if item == 'cl_bracket' and token == ')':
            return True
    return False


def get_next(token: str) -> str:
    """
    This function get token and return what should come next after the token
    :param token: token
    :return: what should come next after the token
    """
    if token in side_of_operands.keys():
        return what_should_come_next.get(side_of_operands.get(token))
    if is_number(token) or token == ')':
        return what_should_come_next.get('operand')
    if token == '(':
        return what_should_come_next.get('both')


def check_right_operators(token_list: list, index: int):
    """
    This function get token list and index and check if there is a right operator after the index before operand
    :param token_list: token list
    :param index: index of the right operator
    :return:
    """
    for i in range(index, len(token_list)):
        if side_of_operands.get(token_list[i]) == 'right':
            throw_exception('right', token_list[i], i)
        elif token_list[i] != '-':
            return None
