import pytest
from calc import parser

import main
from error import ResultIsOutOfScopeError

def test_calc():
    messages = []

    def prn_msg(m: str):
        messages.append(m)
    with pytest.raises(ResultIsOutOfScopeError):
        parser("10000#10#*10000#10#*10000#10#", prn_msg)
