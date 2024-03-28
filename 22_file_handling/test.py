from os import remove
try:
    remove("demofile.txt")
except FileNotFoundError:
    print("The file does not exist")
# else:
#   print("The file does not exist")
# f = open("Gosho.txt", "w")
# f.write("Something2\n")
# f.close()
# v = open("Gosho.txt", "r")
# print(v.read())


#
#
# with open("Stamat.txt", "a") as stamo:
#     stamo.write("Hello Stamo!\n")
#
# with open("stamat.txt") as stamo:
#     print(stamo.read())