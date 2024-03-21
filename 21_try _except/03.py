def float_to_int(n):
    return int(float(n))
number = input()

try:
    print(float_to_int(number))
except ValueError:
    print("You can not make string to integer")