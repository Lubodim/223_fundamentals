from _collections import deque
from datetime import datetime as dt

my_list = []
my_deque = deque()

for num in range(1_000_000):
    my_list.append(num)
    my_deque.append(num)

start = dt.now()
for num in range(10_000):
    my_list.pop(0)
end = dt.now()
print(f"List pop for {end - start} time")

start = dt.now()
for num in range():
    my_deque.popleft()
end = dt.now()
print(f"Deque pop for {end - start} time")
