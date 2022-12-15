from Calculator import calculate
from ExceptionThrower import *


def start():
    """
    This function is the main function of the program
    :return:
    """
    while True:
        print('enter equation or type exit to exit')

        try:
            equation = input()
        except EOFError:
            throw_exception('EOF', exit_program=True)
            exit()
        except KeyboardInterrupt:
            throw_exception('KeyboardInterrupt', exit_program=True)
            exit()
        if equation.lower() == 'exit':
            exit()
        print(calculate(equation))


start()
