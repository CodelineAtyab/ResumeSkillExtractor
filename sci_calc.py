import math


def get_pow(base, exp):
    return math.pow(base, exp)


# For unit tests
if __name__ == "__main__":
    print(get_pow(2, 3))


def get_dividend(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    return dividend / divisor
