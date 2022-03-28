from multiprocessing.sharedctypes import Value


def square(number):
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 1 * 2 ** (number - 1)


def total():
    total = 0
    for i in range(1, 65):
        total += square(i)
    return total
