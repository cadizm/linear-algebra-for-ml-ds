from functools import reduce
import operator

def p_birthday(n):
    """
    Probability that n people have the same birthday
    """
    probabilities = [i / 365. for i in range(365 - n + 1, 365 + 1)]
    return 1 - reduce(operator.mul, probabilities, 1)

if __name__ == '__main__':
    print(p_birthday(30))
