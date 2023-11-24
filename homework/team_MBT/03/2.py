n = int(input())
my_set = set()

for i in range(n):
    command = input().split(", ")

    if command[0] == "IN":
        parking_number = command[1]
        if parking_number not in my_set:
            my_set.add(parking_number)
    elif command[0] == "OUT":
        park_number = command[1]
        if park_number in my_set:
            my_set.remove(park_number)

if not my_set:
    print("Parking lot is Empty!")
else:
    print("\n".join(my_set))