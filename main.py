from Calculator import calculate
from ExceptionThrower import *
from constants import *


def start():
    """
    This function is the main function of the program
    :return:
    """
    print(WELCOME_MESSAGE)
    while True:
        print('Please enter equation or type exit to exit')
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
