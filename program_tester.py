from Calculator import calculate
from ExceptionThrower import error_message_dict


def test_my_program():
    expressions = {'3^*2': 'error', '$4+-7': 'error', '!3+5': 'error', '45(9)': 'error', '9~-3': 'error',
                   'abfdh32^$%#': 'error', '': 'error', '   3+  4   5 +~ -8 ! -7!+-3@5': 35324,
                   '3^2': 9, '(7+~--2)': 5, '-3$2': 2, '-78&32': -78, '45%0': 'error', '-3^0.5': 'error',
                   '213454.54#': 28, '(3^1000)#': 'error', '-45!': 'error', '6!': 720,
                   '5.3!': 'error', '87.543@65.656': 76.5995, '3^1000': 'inf', '45%4': 1, '34/0': 'error',
                   '13  2+--4  5*-(21+(5/ 1 5 +3 ^2))+-~-5$3': -1238, '(~- 7!   &100 0!!/-(2 +--3)*6)##/2+78': 73.5}
    print('\n\n')
    for equation in expressions.keys():
        print(equation, end=' =')
        assert calculate(equation) == expressions.get(equation)
        print()
