# задача * 9:
# names_stack = []
# while True:  # while name_of_the_client!="END"
#     name_of_the_client = input()
#
#     if name_of_the_client == "PAID":
#         while names_stack:
#             print(names_stack.pop(0))
#
#     elif name_of_the_client == "END":
#         break
#     else:
#         names_stack.append(name_of_the_client)
#
# print(f"{len(names_stack)} people remaining.")
#
# задача * 9
# втори
# начин
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
#
# задача * 10:
start_quantity_nuggets = int(input())
queue = []
name_of_the_person = input()
while name_of_the_person != "Start":
    queue.append(name_of_the_person)
    name_of_the_person = input()
command2 = input()
while command2 != "End":
    taken_bites = command2
    if taken_bites.isdigit():

        taken_bites = int(taken_bites)
        if start_quantity_nuggets >= taken_bites:
            current_name = queue.pop(0)
            print(f"{current_name} takes bites.")
            start_quantity_nuggets -= taken_bites

        else:
            current_name = queue.pop(0)
            print(f"{current_name} must wait.")

    elif taken_bites.startswith("refill"):
        current_bites = command2.split()
        current_bites = int(current_bites[1])
        start_quantity_nuggets += current_bites

    command2 = input()

print(f"{abs(start_quantity_nuggets)} bites has left.")

# задача * 11:
# names_of_the_people = input().split()
# number = int(input())
# current_index = 0
#
# while len(names_of_the_people) > 1:
#     current_index = (current_index + number - 1) % len(names_of_the_people)
#     remove = names_of_the_people.pop(current_index)
#     print(f"Removed {remove}")
# the_last_person = names_of_the_people[0]
# print(f"The winner is {the_last_person}.")

