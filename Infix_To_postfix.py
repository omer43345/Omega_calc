from constants import *


def postfix_convertor(token_list: list) -> list:
    """
    This function converts the token list infix expression to postfix list expression
    :param token_list: token list of the infix expression
    :return: postfix list expression
    """
    stack = []
    postfix_list = []
    index = 0
    while index < len(token_list):
        if is_number(token_list[index]):
            postfix_list.append(token_list[index])
        elif token_list[index] == '(':
            stack.append('(')
        elif token_list[index] == ')':
            while stack and stack[-1] != '(':
                postfix_list += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority_dict[token_list[index]] <= priority_dict[stack[-1]]:
                postfix_list += stack.pop()
            stack.append(token_list[index])
        index += 1
    while stack:
        postfix_list += stack.pop()
    return postfix_list


def postfixSolver(exp: list) -> int:
    """
    This function solves the postfix expression
    :param exp: postfix expression
    :return: the result of the expression
    """
    stack = []
    for character in exp:
        if is_number(character):
            stack.append(character)
        else:
            val1 = stack.pop()
            if side_of_operands[character] == 'both':
                val2 = stack.pop()
                stack.append(operators_functions_dict[character](float(val2), float(val1)))
            else:
                stack.append(operators_functions_dict[character](float(val1)))
    return stack.pop()


