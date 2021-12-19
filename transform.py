
from error import RadixIsOutOfScopeError, NumberIsOutOfScopeError

def is_radix_out_of_scope(radix):
    return radix > 16 or radix < 2


def is_number_out_of_scope(number, radix):
    num = int(convert_base(number, to_base=10, from_base=radix))
    return num > 10000 or num < 0

def convert_base(num: str, to_base: int =10, from_base: int =10) -> str:
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def transform_mode(print_func, input_func=input, format_func=None):
    print_func("Congrats! you are in transform mode right now :)")
    print_func("Please input the basic radix: ")
    basic_radix = int(input_func())
    if is_radix_out_of_scope(basic_radix):
        print_func("Radix is out of scope")
        return

    print_func("Please enter the final radix: ")
    final_radix = int(input_func())
    if is_radix_out_of_scope(final_radix):
        print_func("Radix is out of scope")
        return

    print_func("Please enter the number to transform: ")

    number = input_func()
    if is_number_out_of_scope(number, basic_radix):
        print_func("Number is out of scope")
        return

    output = convert_base(number, final_radix, basic_radix)
    print_func(format_func(output))


