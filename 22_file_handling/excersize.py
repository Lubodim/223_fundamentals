import os
if os.path.exists("data.txt"):
    os.remove("data.txt")
else:
    print("That file does not exist")

try:
    os.remove("output.txt")
except FileNotFoundError:
    print("That file does not exist")
#2
# with open("data.txt", "a") as kamak:
#     while True:
#         some_text = input("Enter a text: ")
#         if some_text == "end":
#             break
#         kamak.write(f"{some_text}\n")
# with open("data.txt", "r") as kamak:
#     print(kamak.read())
#
#



#1
# with open("output.txt", "w") as ou:
#     ou.write("Some text\n")
#
# with open("output.txt", "r") as ou:
#     print(ou.read())
