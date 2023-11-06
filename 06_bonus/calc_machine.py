

def calc(num_1, num_2, operator):
    if operator in ["/", "//", "%"] and num_2 == 0:
        return "Number must be different from ZERO! Try again! "

    my_calc = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "**": lambda x, y: x ** y,
        "/": lambda x, y: x / y,
        "//": lambda x, y: x // y,
        "%": lambda x, y: x % y,

    }

    result = my_calc[operator](num_1, num_2)
    return f"{num_1} {operator} {num_2} = {result}"


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2

def grading(num1, num2):
    return num1 ** num2

def divide(num1, num2):
    return num1 / num2

def integer_divide(num1, num2):
    return num1 // num2

def modulo_divide(num1, num2):
    return num1 % num2

def calc_2(num_1, num_2, operator):
    if operator in ["/", "//", "%"] and num_2 == 0:
        return "Number must be different from ZERO! Try again! "

    my_calc = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "**": grading,
        "/": divide,
        "//": integer_divide,
        "%": modulo_divide,

    }

    result = my_calc[operator](num_1, num_2)
    return f"{num_1} {operator} {num_2} = {result}"