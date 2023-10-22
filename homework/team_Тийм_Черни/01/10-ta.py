bites = int(input())
guests = []

while True:
    command = input()

    if command == "Start".lower():
        break

    guests.append(command)

while True:
    command = input()

    if command.startswith("refill"):
        beets = command.split()
        bites += int(beets)
    else:
        bites = int(command)
        if bites >= bites:
            guest = guests.pop(0)
            bites -= bites
            print(f"{guest} take bites")
        else:
            guest = guests.pop(0)
            print(f"{guest} must wait")
        if command == "End".lower():
            break

print(f"{bites} bites left")