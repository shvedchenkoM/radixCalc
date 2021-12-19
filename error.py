# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class UnexpectedModeError(Error):
    """Raised when user had inputed incorrect mode"""
    pass


class RadixIsOutOfScopeError(Error):
    """Raised when the input radix is out of scope"""
    pass

class NumberIsOutOfScopeError(Error):
    """Raised when the input number is out of scope"""
    pass

class ResultIsOutOfScopeError(Error):
    """Raised when the input number is out of scope"""
    pass

class UnexpectedOperatorError(Error):
    """Raised when the input number is out of scope"""
    pass

class NoEqualSignError(Error):
    pass