from Calculator import calculate
from ExceptionThrower import *


def start():
    """
    This function is the main function of the program
    :return:
    """
    while True:
        print('enter equation or type exit to exit')
        equation = ''
        try:
            equation = input()
        except EOFError:
            throw_exception('EOF', exit_program=True)
        except KeyboardInterrupt:
            throw_exception('KeyboardInterrupt', exit_program=True)
        if equation.lower() == 'exit':
            exit()
        calculate(equation)


start()
