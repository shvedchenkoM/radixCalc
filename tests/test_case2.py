import pytest
from calc import calc_mode

import main
from error import NoEqualSignError

def test_calc():
    messages = []

    def prn_msg(m: str):
        messages.append(m)

    def input_gen():
        yield from ["10#10#*10#10#*10#10#="]

    input_gen_inv = input_gen()

    def input_func():
        return next(input_gen_inv)

    assert calc_mode(print_func=prn_msg, input_func=input_func) == 1000
            
