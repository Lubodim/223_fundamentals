def divide(a, b):
    return int(a) / int(b)
try:
    num1, num2 = input().split(", ")
except ValueError:
    print("You must input 2 numbers")
try:
    print(divide(num1, num2))
except ZeroDivisionError:
    print("You can not divide by zero")
except ValueError:
    print("You can not divide by characters")
except NameError:
    print("You can not use empty strings")