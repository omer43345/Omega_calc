from Validator import check_bracket_and_get_cl_bracket_index
from constants import *

"""
This file contains the function that remove the minuses that are not needed
and change the operators and signs that need to be changed because of the minuses
"""


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
    if token_list[index - 1] in operators_that_changing_sign:
        token_list[index - 1] = operators_that_changing_sign[
            (operators_that_changing_sign.index(token_list[index - 1]) + 1) % 2]
    else:
        token_list = insert_unary_minus(index, token_list)
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
