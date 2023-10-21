from collections import deque
queue = deque()

while True:
    customer = input()

    if customer == "PAID":
        for person in queue:
            print(person)
        queue.clear()
    if customer == "END":
        remaining = len(queue)
        print(f"{remaining} people remaining.")
        break
    else:
        queue.append(customer)