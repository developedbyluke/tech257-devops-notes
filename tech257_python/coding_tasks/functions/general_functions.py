# Why use functions?
# Principle: DRY (Don't Repeat Yourself)

def print_something():
    print("Hello world!")


def addition(num1: int, num2: int) -> int:
    return num1 + num2


def multi_args(*args) -> tuple:
    return args


print(multi_args(1, 2, 3))
