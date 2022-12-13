from constants import *


def postfix_convertor(token_list: list) -> str:
    stack = []
    output = []
    index = 0
    while index < len(token_list):
        if is_number(token_list[index]):
            output.append(token_list[index])
        elif token_list[index] == '(':
            stack.append('(')
        elif token_list[index] == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority_dict[token_list[index]] <= priority_dict[stack[-1]]:
                output += stack.pop()
            stack.append(token_list[index])
        index += 1
    while stack:
        output += stack.pop()

    return output


def postfixSolver(exp: list) -> int:
    stack = []
    for character in exp:
        if is_number(character):
            stack.append(character)
        else:
            val1 = stack.pop()
            if side_of_operands[character] == 'both':
                val2 = stack.pop()
                stack.append(operators_dict[character](float(val2), float(val1)))
            else:
                stack.append(operators_dict[character](float(val1)))

    return stack.pop()

