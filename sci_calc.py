import math


def sum(a, b):
    return a + b


def diff(num1, num2):
    return num1 - num2


def get_abs(x):
    return abs(x)


def sqrt(num):
    return math.sqrt(num)


def get_pow(base, exp):
    return math.pow(base, exp)


def get_dividend(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    return dividend / divisor


# For unit tests
if __name__ == "__main__":
    print(get_pow(2, 3))
    print(get_dividend(10, 2))
    # print(get_dividend(5, 0))


def get_bin(n):
    return (bin(n))
