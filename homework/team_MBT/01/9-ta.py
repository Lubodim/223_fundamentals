# задача * 9:
names_stack = []
while True:  # while name_of_the_client!="END"
    name_of_the_client = input()

    if name_of_the_client == "PAID":
        while names_stack:
            print(names_stack.pop(0))

    elif name_of_the_client == "END":
        break
    else:
        names_stack.append(name_of_the_client)

print(f"{len(names_stack)} people remaining.")


# задача * 9
# втори начин
# names_stack = []
# while True:  # while name_of_the_client!="END"
#     name_of_the_client = input()
#     if name_of_the_client != "PAID" and name_of_the_client != "END":
#         names_stack.append(name_of_the_client)
#     elif name_of_the_client == "PAID":
#         while names_stack:
#             print(names_stack.pop(0))
#
#     elif name_of_the_client == "END":
#         break
#
# print(f"{len(names_stack)} people remaining.")