
from collections import deque

pallet_with_clothes = input().split()
pallet_with_clothes = [int(cloth) for cloth in pallet_with_clothes]

shelf_capacity = int(input())

current_shelf = deque()

shelf_count = 0

for cloth in pallet_with_clothes:
    if sum(current_shelf) + cloth <= shelf_capacity:
        current_shelf.append(cloth)
    else:
        shelf_count += 1
        current_shelf = deque([cloth])

if current_shelf:
    shelf_count += 1

print(shelf_count)