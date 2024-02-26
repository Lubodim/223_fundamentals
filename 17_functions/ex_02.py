from math import sqrt


def square_root(num):
    return sqrt(num)


numbers = [float(el) for el in input().split()]
for num in numbers:
    print(f"Square of {num} is {square_root(num):.2f}")
