__all__ = [
    "Number",
    "initial_numbers",
]


class Number:
    """A class that represents some concrete expression and its evaluated value."""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} = {self.value}"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.name == other.name
        return False


# Some interesting numbers to start with
initial_numbers = [
    # Euler's number
    Number("e", 2.718281828459045),
    # The golden ratio
    Number("φ", 1.618033988749895),
    # The ratio of a circle's circumference to its diameter
    Number("τ", 6.283185307179586),
    # Half of tau
    Number("π", 3.141592653589793),
    # Two interesting square roots
    Number("√2", 1.414213562373095),
    Number("√3", 1.732050807568877),
    # We don't want to have the zeta function as an operation because its
    # range extends beyond the reals for many inputs and it is
    # frequently multivalued. But we can stil have it in the output
    # by just using this particular well-behaved input value.
    # Fun fact, this is equal to the sum of the reciprocals of the
    # natural numbers.
    Number("ζ(−1)", -0.08333333333),
] + [Number(str(i), i) for i in range(-10, 12) if i != 0]
