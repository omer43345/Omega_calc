from TokenList import *
from Validator import validate
from Infix_To_postfix import *
from minus_handler import remove_unwanted_minuses


def calculate(equation: str):
    """
    This function get equation as string and calculate the equation if it is valid and print the result or the error message
    :param equation: equation as string
    :return: the result of the equation or error
    """
    token_list = token_list_convertor(equation)
    for token in token_list:
        print(token, end='')
    print('=>', end=' ')
    try:
        validate(token_list)
        token_list = remove_unwanted_minuses(token_list)
        res = postfixSolver(postfix_convertor(token_list))
        print(str(res))
    except Exception as e:
        print(e)
        return 'error'
    return res
