import math

def multiply(num1, num2):
    result = num1 * num2
    return result



def get_pow(base, exp):
    return math.pow(base, exp)


# For unit tests
if __name__ == "__main__":
    print(get_pow(2, 3))
    print(multiply(4, 4))

