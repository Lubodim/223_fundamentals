def divide(a,b):
    return int(a) / int(b)
try:
    num1, num2 = input().split(", ")
except ValueError:
    print("You need to add 2 numbers")
try:
    print(divide(num1, num2))
except ZeroDivisionError:
    print("You cannot divide by 0")
except ValueError:
    print("You cannot divide by characters")
except NameError:
    print("You cant use empty str")