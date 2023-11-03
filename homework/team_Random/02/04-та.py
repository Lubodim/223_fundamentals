from collections import deque
clothes = list(map(int, input().split()))
capacity = int(input())

racks_count = 0
current_rack_sum = 0
current_rack = deque()

for cloth in clothes:
    if current_rack_sum + cloth <= capacity:
        current_rack_sum += cloth
        current_rack.append(cloth)
    else:
        racks_count += 1
        current_rack_sum = cloth
        current_rack = deque([cloth])

if len(current_rack) > 0:
    racks_count += 1

print(racks_count)