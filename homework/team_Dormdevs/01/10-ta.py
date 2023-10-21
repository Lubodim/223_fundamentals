from collections import deque

initial_bites = int(input())
queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill"):
        command_parts = command.split()
        command_type = command_parts[0]
        beets = int(command_parts[1])
        initial_bites += beets
    else:
        requested_bites = int(command)
        if not queue:
            continue
        person = queue.popleft()
        if requested_bites <= initial_bites:
            print(f"{person} take {requested_bites} bites")
            initial_bites -= requested_bites
        else:
            print(f"{person} must wait")

print(f"{initial_bites} bites left")