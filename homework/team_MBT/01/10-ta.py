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