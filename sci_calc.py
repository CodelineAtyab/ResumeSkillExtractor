import math
def sum(a,b):
    return a+b

def get_abs(x):
    return abs(x)

def sqrt(num):
    return math.sqrt(num)


def get_pow(base, exp):
    return math.pow(base, exp)


# For unit tests
if __name__ == "__main__":
    print(get_pow(2, 3))
