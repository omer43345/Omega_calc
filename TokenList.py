def token_list_convertor(equation: str) -> list:
    """
    This function get equation as string and converts the equation to a list of tokens
    :param equation: equation as string
    :return: tokens list of the equation
    """
    token_list = ['']
    char_index = 0
    while char_index < len(equation):
        if equation[char_index].isnumeric() or equation[char_index] == '.':
            # if the char is a number or a dot add it to the last token
            token_list[len(token_list) - 1] += (equation[char_index])
        else:
            token_list.append(equation[char_index])
            token_list.append('')
        char_index += 1
    token_list = list(filter(lambda x: x != '', token_list))
    token_list = list(filter(lambda x: x != ' ', token_list))
    print(token_list)
    return token_list


expression = '  1236+43-(- 1.5)*(-2.5)'
tokens_list = token_list_convertor(expression)
