from TokenList import *
from Validator import validate
from Infix_To_postfix import *


def calculate(equation: str):
    """
    This function get equation as string and calculate the equation if it is valid and print the result or the error message
    :param equation: equation as string
    :return: the result of the equation or error
    """
    try:
        token_list = validate(token_list_convertor(equation))
        res = postfixSolver(postfix_convertor(token_list))
        print('The result is: ' + str(res))
    except Exception as e:
        print(e)
        return 'error'
    return res
