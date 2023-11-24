N = int(input("Enter the number of actions: "))

parking = set()

for _ in range(N):
    action, plate = input().split(", ")

    if action == "IN":
        parking.add(plate)
    elif action == "OUT" and plate in parking:
        parking.remove(plate)

if parking:
    print(*parking, sep="\n")
else:
    print("Parking is Empty")