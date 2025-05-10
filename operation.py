from functools import lru_cache
from math import gamma, log, tan

# There's part of me that wants to have a base class for operations
# but all of their functions take different numbers of arguments
# so it seems actually uglier to try to shoehorn that in.
# I'm open to ideas on how to accomplish that elegantly.


class UnaryOperation:
    """A class representing a unary operation."""

    def __init__(
        self,
        name,
        func,
        renderer,
        validator=lambda _: True,
    ):
        self.name = name
        self.func = func
        self.renderer = renderer
        self.validator = validator

    def is_binary(self):
        return False

    @lru_cache(maxsize=None)
    def operate(self, x):
        return self.func(x.value)

    @lru_cache(maxsize=None)
    def render(self, x):
        return self.renderer(x.name)

    @lru_cache(maxsize=None)
    def validate(self, x):
        return self.validator(x.value)


class BinaryOperation:
    """A class representing a binary operation."""

    def __init__(
        self,
        name,
        func,
        renderer,
        validator=lambda _x, _y: True,
        commutes=False,
    ):
        self.name = name
        self.func = func
        self.renderer = renderer
        self.validator = validator
        self.commutes = commutes

    def is_binary(self):
        return True

    @lru_cache(maxsize=None)
    def operate(self, x, y):
        return self.func(x.value, y.value)

    @lru_cache(maxsize=None)
    def render(self, x, y):
        return self.renderer(x.name, y.name)

    @lru_cache(maxsize=None)
    def validate(self, x, y):
        return self.validator(x.value, y.value)


operations = [
    # Absolute value
    UnaryOperation(
        "abs",
        lambda x: abs(x),
        lambda x: f"|{x}|",
        # Disallow positive numbers, not because it will break anything,
        # but because it's pointless.
        validator=lambda x: x < 0,
    ),
    # Addition
    BinaryOperation(
        "add",
        lambda x, y: x + y,
        lambda x, y: f"({x}) + ({y})",
        commutes=True,
    ),
    # Division
    BinaryOperation(
        "div",
        lambda x, y: x / y,
        lambda x, y: f"({x}) / ({y})",
        # Disallow division by zero
        lambda _, y: y != 0,
    ),
    # Gamma function, the analytic continuation of the factorial function
    UnaryOperation(
        "gamma",
        lambda x: gamma(x),
        lambda x: f"Γ({x})",
        # Disallow negative values
        lambda x: x > 0,
    ),
    # Natural logarithm (called log in Python for some abominable reason)
    UnaryOperation(
        "ln",
        lambda x: log(x),
        lambda x: f"ln({x})",
        # Disallow negative values
        lambda x: x > 0,
    ),
    # Modulus
    BinaryOperation(
        "mod",
        lambda x, y: x % y,
        lambda x, y: f"({x}) % ({y})",
        # Disallow division by zero
        lambda _, y: y != 0,
    ),
    # Multiplication
    BinaryOperation(
        "mul",
        lambda x, y: x * y,
        lambda x, y: f"({x}) * ({y})",
        commutes=True,
    ),
    # Exponentiation
    BinaryOperation(
        "pow",
        lambda x, y: x**y,
        lambda x, y: f"({x})^({y})",
        lambda x, y: not (x == 0 and y < 0) and (x >= 0 or y % 1 == 0),
    ),
    # Square root
    UnaryOperation(
        "sqrt",
        lambda x: x**0.5,
        lambda x: f"√({x})",
        # No complex analysis zone
        lambda x: x >= 0,
    ),
    # Subtraction
    BinaryOperation(
        "sub",
        lambda x, y: x - y,
        lambda x, y: f"({x}) - ({y})",
    ),
    # Trigonometric tangent function
    # We're not doing sin and cos because they are periodic
    # on a very limited range, and thus not interesting.
    UnaryOperation(
        "tan",
        lambda x: tan(x),
        lambda x: f"tan({x})",
    ),
]
