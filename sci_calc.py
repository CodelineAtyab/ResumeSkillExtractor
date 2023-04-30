import math


def get_dividend(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    return dividend / divisor


# For unit tests
if __name__ == "__main__":
    print(get_dividend(10, 2))
    print(get_dividend(5, 0))
