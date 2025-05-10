import sys
from contextlib import suppress
from functools import lru_cache
from itertools import combinations
from random import shuffle

from number import Number, initial_numbers
from operation import operations

min, max = sys.argv[1:3]
min = float(min)
max = float(max)


@lru_cache(maxsize=None)
def check(candidate):
    """Check to see if a given number is in the target range and print it."""
    if candidate.value > min and candidate.value < max:
        print(str(candidate))


def elide(list_, *indices):
    """Remove elements from a list at the given indices."""
    return [x for i, x in enumerate(list_) if i not in indices]


def give_it_a_go(numbers, ops):
    """Recursively try to combine numbers and operations to find a solution."""
    if not numbers or not ops:
        return
    shuffle(numbers)
    shuffle(ops)
    for i in range(len(ops)):
        op = ops[i]
        # For binary operations, we need to pick two numbers
        if op.is_binary():
            for j, k in combinations(range(len(numbers)), 2):
                a, b = numbers[j], numbers[k]
                if op.validate(a, b):
                    # Just ignore overflow errors
                    with suppress(OverflowError):
                        result = Number(
                            op.render(a, b),
                            op.operate(a, b),
                        )
                        check(result)
                        give_it_a_go(
                            elide(numbers, j, k) + [result],
                            elide(ops, i),
                        )
                # We only need to try the reverse if the operation doesn't commute
                if not op.commutes:
                    if op.validate(b, a):
                        with suppress(OverflowError):
                            result = Number(
                                op.render(b, a),
                                op.operate(b, a),
                            )
                            check(result)
                            give_it_a_go(
                                elide(numbers, j, k) + [result],
                                elide(ops, i),
                            )
        else:
            # This code could be simpler if all operations were unary, but that would be boring.
            for j in range(len(numbers)):
                a = numbers[j]
                if not op.validate(a):
                    continue
                result = Number(
                    op.render(a),
                    op.operate(a),
                )
                check(result)
                give_it_a_go(
                    elide(numbers, j) + [result],
                    elide(ops, i),
                )


# Kick off the recursive search
give_it_a_go(initial_numbers, operations)
