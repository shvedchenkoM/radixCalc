import pytest

import main


@pytest.mark.parametrize("inp,from_rx,to_rx,exp_res, error_msg", [
    ("38", "10", "2", "100110", None)
])
def test_transform(inp, from_rx, to_rx, exp_res, error_msg):
    from transform import transform_mode

    messages = []

    def prn_msg(m: str):
        messages.append(m)

    def input_gen():
        yield from [from_rx, to_rx, inp]

    input_gen_inv = input_gen()

    def input_func():
        return next(input_gen_inv)

    transform_mode(print_func=prn_msg, input_func=input_func, format_func=main.get_output)
    if error_msg is None:
        assert messages == ['Congrats! you are in transform mode right now :)', 'Please input the basic radix: ', "Please enter the final radix: ", 'Please enter the number to transform: ',
                            f'Your answer is {exp_res} :)']
    else:
        error_msg in messages
