from collections import deque

children = input().split()
n = int(input())
queue = deque(children)

while len(queue) > 1:
    for i in range(n - 1):
        queue.append(queue.popleft())
    removed_child = queue.popleft()
    print(f"Removed {removed_child}")

winner = queue.popleft()
print(f"Winner is {winner}")
