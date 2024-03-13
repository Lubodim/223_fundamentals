num1, num2, operatop = [float(i) if i.isdigit() else str(i) for i in input().split()]

if operatop == "+":
    result = lambda x, y: x + y
elif operatop == "-":
    result = lambda x, y: x - y
elif operatop == "*":
    result = lambda x, y: x * y
elif operatop == "/":
    result = lambda x, y: "Error" if y == 0 else x / y

print(result(num1, num2))
