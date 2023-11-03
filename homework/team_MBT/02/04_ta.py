from collections import deque

clothes = deque(map(int, input().split()))
capcacity = int(input())
number_capacites = 0
current_capacity = 0
for clothe in clothes:

    if number_capacites + int(clothe) > capcacity:
        current_capacity += 1
        number_capacites = 0
    number_capacites += int(clothe)
if number_capacites > 0:
    current_capacity += 1

print(current_capacity)