def float_to_int(n):
    return int(n)

try:
    number =float(input())
    print(float_to_int(number))
except ValueError:
    print("You cannot make str to int")