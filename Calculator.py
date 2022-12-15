from TokenList import *
from Validator import validate
from Infix_To_postfix import *


def calculate(equation: str):
    """
    This function get equation as string and calculate the equation if it is valid
    :param equation: equation as string
    :return: the result of the equation
    """
    token_list = validate(token_list_convertor(equation))
    return postfixSolver(postfix_convertor(token_list))

