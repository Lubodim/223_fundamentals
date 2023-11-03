from collections import deque
food = int(input())
my_deque = deque(map(int, input().split(" ")))

print(max(my_deque))

while my_deque:
    order = my_deque.popleft()
    if food >= order:
        food -= order
    else:
        my_deque.appendleft(order)
        break

if my_deque:
    print(f"Orders left: {', '.join(map(str, my_deque))}")
else:
    print("Orders complete")