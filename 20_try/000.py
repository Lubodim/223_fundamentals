def divide(a, b):
    return int(a) / int(b)
while True:
    num1 = input()
    num2 = input()
    try:
        print(divide(num1, num2))
    except ZeroDivisionError:
        print("You can't divide by zero")
    except ValueError:
        print("You can't divide by characters")
    else:
        print("Divide is successful")
    finally:
        print("This is my calculation")