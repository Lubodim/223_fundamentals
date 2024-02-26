def add(num1, num2):
    result = num1 + num2
    return result


def subtract(num1, num2):
    result = num1 - num2
    return result


def multiply(num1, num2):
    result = num1 * num2
    return result


def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by 0!"
    result = num1 / num2
    return result


def main_func():
    while True:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        operator = input("Choice between + - * / or Stop for END: ")
        if operator.lower() == "Stop":
            break
        elif operator == "+":
            total = add(number1, number2)
        elif operator == "-":
            total = subtract(number1, number2)
        elif operator == "*":
            total = multiply(number1, number2)
        elif operator == "/":
            total = divide(number1, number2)
        else:
            print("Unknown operator")
            continue
        return total


print(main_func())
