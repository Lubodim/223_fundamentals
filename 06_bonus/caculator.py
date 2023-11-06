from calc_machine import calc, calc_2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operators = input("Choice one operator from '+, -, *, **, /, //, %': ")


# print(calc(num1, num2, operators))
print(calc_2(num1, num2, operators))






#
# if operators == "+":
#     print(f"{num1} {operators} {num2} = {num1 + num2}")
# elif operators == "-":
#     print(f"{num1} {operators} {num2} = {num1 - num2}")
# elif operators == "*":
#     print(f"{num1} {operators} {num2} = {num1 * num2}")
# elif operators == "**":
#     print(f"{num1} {operators} {num2} = {num1 ** num2}")
# elif operators == "/":
#     if num2 == 0:
#         print("Number must be different from ZERO! Try again! ")
#     else:
#         print(f"{num1} {operators} {num2} = {num1 / num2}")
# elif operators == "//":
#     if num2 == 0:
#         print("Number must be different from ZERO! Try again! ")
#     else:
#         print(f"{num1} {operators} {num2} = {num1 / num2}")
# elif operators == "%":
#     if num2 == 0:
#         print("Number must be different from ZERO! Try again! ")
#     else:
#         print(f"{num1} {operators} {num2} = {num1 / num2}")

