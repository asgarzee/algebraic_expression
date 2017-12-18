import re
import sys


def parse_expression_and_variables(equation):
    vars_list = re.findall('[a-z]+=[0-9]+[\.]?[0-9]+', equation)
    expression_list = re.findall('[a-z]*[\+\-\/\*\(\)][\(]?[a-z]+[\)]?', equation)
    expression = ''.join(expression_list)
    var_dict = {var.split('=')[0]: var.split('=')[1] for var in vars_list}
    for var, value in var_dict.items():
        expression = expression.replace(var, value)
    return expression


def evaluate_expression(equation):
    """
    Eqation should be a string of algebraic expression and variables with its values separated by space
    Example :
    equation : a='(a+b)+c a=3 b=4 c=5'
    :param equation:
    :return:
    """
    expression = parse_expression_and_variables(equation.strip().lower())
    result = eval(expression)
    print(result)
    return result


if __name__ == '__main__':
    evaluate_expression(sys.argv[1])
