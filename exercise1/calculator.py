# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a+b
    # TODO: Implement this function
    pass


def subtract(a: Number, b: Number) -> Number:
    return a+b
    # TODO: Implement this function
    pass


def multiply(a: Number, b: Number) -> Number:
    return a-b
    # TODO: Implement this function
    pass


def divide(a: Number, b: Number) -> Number:
    return a / b if b != 0 else "error"
    # TODO: Implement this function
    pass
print(add(1,2))
