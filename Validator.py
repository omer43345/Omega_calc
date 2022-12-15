from constants import *
from ExceptionThrower import throw_exception


def validate(token_list: list) -> list:
    """
    This function get token list and validate it
    :param token_list: token list
    :return: token list
    """
    char_validation(token_list)
    check_brackets(token_list)
    token_list = remove_unwanted_minuses(token_list)
    token_list_validator(token_list)
    return token_list


def char_validation(token_list: list):
    """
    This function get token list and check if there is a char that is not a valid char
    :param token_list: token list
    :return:
    """
    for token in token_list:
        if not (is_number(token) or operators_dict.get(token) or token in ['(', ')']):
            throw_exception('unknown_char', token_list.index(token))


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
        elif token_list[index] == ')':
            throw_exception('brackets')
        index += 1


def check_bracket_and_get_cl_bracket_index(token_list: list, index: int) -> int:
    """
    This function get token list and index and check if there is a problem the bracket that start in index
    :param token_list: token list
    :param index: index of the bracket
    :return: index of the closing bracket
    """
    num_of_brackets = 1
    while index < len(token_list) and num_of_brackets > 0:
        if token_list[index] == '(':
            num_of_brackets += 1
        elif token_list[index] == ')':
            num_of_brackets -= 1
        index += 1
    if num_of_brackets == 0:
        return index
    throw_exception('brackets')


def token_list_validator(token_list: list):
    """
    This function get token list and check if there is a problem with the token list by checking what should come next after each token
    :param token_list: token list
    :return:
    """
    next_item = 'operand.op_bracket.right'
    if len(token_list) == 0 or not(any(is_number(token) for token in token_list)):
        throw_exception('empty')
    index = 0
    for token in token_list:
        list_next = next_item.split('.')
        if not is_token_valid(list_next, token):
            if token == token_list[- 1]:
                throw_exception('extra_token')
            throw_exception(get_reason(token), index)
        next_item = get_next(token)
        index += 1
    if what_should_come_next.get('operand') != next_item:
        throw_exception('extra_token')


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


def remove_unwanted_minuses(token_list: list) -> list:
    """
    This function get token list and remove the minuses that are not needed
    :param token_list: token list
    :return: token list without the minuses that are not needed
    """
    index = 0
    while index < len(token_list):
        if token_list[index] == '-' and (index == 0 or can_remove_minus(token_list[index - 1])):
            [token_list, should_change_list] = remove_minuses(index, token_list)
            if should_change_list and index < len(token_list):
                token_list = change_operator_or_sign(index, token_list)
        index += 1
    return token_list


def remove_minuses(index: int, token_list: list) -> list:
    """
    This function get index and token list and remove the minuses that are not needed from the index
    :param index: index
    :param token_list: token list
    :return: token list without the minuses that are not needed from the index
    """
    should_change_list = False
    while index < len(token_list) and token_list[index] == '-':
        token_list.pop(index)
        should_change_list = not should_change_list
    return [token_list, should_change_list]


def can_remove_minus(token: str) -> bool:
    # this function get token before the minus and check if the minus can be removed
    return side_of_operands.get(token) in ['both', 'right'] or token == '('


def change_operator_or_sign(index: int, token_list: list) -> list:
    """
    This function get index and token list and change the operator or sign
    :param index: index
    :param token_list: token list
    :return: token list with the changed operator or sign
    """
    if index == 0 or token_list[index - 1] not in operators_that_changing_sign or token_list[index - 1] == '(':
        token_list = insert_unary_minus(index, token_list)
    elif token_list[index - 1] in operators_that_changing_sign:
        token_list[index - 1] = '+' if token_list[index - 1] == '-' else '-'
    return token_list


def insert_unary_minus(index: int, token_list: list) -> list:
    """
    This function get index and token list and insert unary minus
    :param index: index
    :param token_list: token list
    :return: token list with the inserted unary minus
    """
    if token_list[index] == '(':
        token_list.insert(index, '(')
        token_list.insert(index + 1, '-1')
        token_list.insert(index + 2, '*')
        token_list.insert(check_bracket_and_get_cl_bracket_index(token_list, index + 4), ')')
    elif is_number(token_list[index]):
        token_list[index] = str(float(token_list[index]) * -1)
    elif side_of_operands.get(token_list[index]) == 'right':
        token_list.insert(index + 1, '-')
    return token_list
