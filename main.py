from calc import calc_mode
from error import UnexpectedModeError
from transform import transform_mode


def get_output(name):
    return f"Your answer is {name} :)"

def print_msg(msg):
    # Use a breakpoint in the code line below to debug your script.
    print(msg)  # Press Ctrl+F8 to toggle the breakpoint.

def print_program_desc():
    return "Hi there and welcome to VRNC! " \
           "VRNC is a console calculator that provides the ability " \
           "to do the operations between numbers with different radixes." \
           "VRNC  accepts a string in the input field - an arithmetic expression, " \
           "where operands are positive numbers less than 10000 (with any radix " \
           "specified in the range from 2 to 16) number system, " \
           "operations - `+`, `-`,` * `, `/`. + The ability to display the answer " \
           "in any convenient (required) number system. " \
           "The system should, if necessary, clarify the radix of a number " \
           "if it has not been specified by the user. "

def get_mode(mode: str, calc_f, trans_f):
    if mode == "transform":
        trans_f(print_msg, format_func=get_output)
    elif mode == "calc":
        calc_f(print_msg, format_func=get_output)
    else:
        raise UnexpectedModeError()

def main():
    print_msg(print_program_desc())
    try:
        mode = input("Please input your mode: ")
        get_mode(mode, calc_f=calc_mode, trans_f=transform_mode)
    except UnexpectedModeError:
        print("Не корректный режим использования приложения")
        exit(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
