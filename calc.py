import transform
from error import ResultIsOutOfScopeError, UnexpectedOperatorError, NoEqualSignError


def pars_and_transform_tuple(tuple):
    num, rad, et = tuple.split("#")
    if rad == None:
        return int(num)
    else:
        rad = int(rad)
    return int(transform.convert_base(num, 10, rad))

def is_result_out_of_scope(number):
    return number > 100000000 or number < 0



def parser(input, print_func):
    input = '+' + input

    result = 0
    my_slices = input.split('#')[:-1]
    for i in range(len(my_slices)//2):
        sign = my_slices[i*2][0]
        digit = my_slices[i*2][1:]
        radix = int(my_slices[i*2+1])
        if transform.is_radix_out_of_scope(radix):
            print_func("Radix is out of scope")
            return

        if transform.is_number_out_of_scope(digit, radix):
            print_func("Number is out of scope")
            return

        conv_val = int(transform.convert_base(digit, 10, radix))
        if sign == "+":
            result = result + conv_val
        elif sign == "-":
            result = result - conv_val
        elif sign == "*":
            result = result * conv_val
        elif sign == "/":
            result = result // conv_val
        else:
            raise UnexpectedOperatorError("Unexpected operator")
    if is_result_out_of_scope(result):
        raise ResultIsOutOfScopeError("Result is out of scope")

    return result

def calc_mode(print_func, input_func=input, calc_func=None):
    print_func("Congrats! you are in calculate mode right now :)")
    print_func("Please input the expression: ")
    equation = input_func()
    if '=' not in equation:
        raise NoEqualSignError("There is no equal sign.")
        print_func(f"There is no symbol = in {equation}")
        return
    else:
        before_eq, after_eq = equation.split("=")
    answ = parser(before_eq, print_func)
    if after_eq == '':
        return answ
    else:
        new_rad = int(after_eq[1:len(after_eq)-1])
        return transform.convert_base(answ, new_rad, 10)
