from collections import deque

quantity_of_food_for_the_day = int(input())
quantity_food_for_every_order = deque(map(int,input().split()))
max_num = max(quantity_food_for_every_order)
while quantity_food_for_every_order:
    current_order = quantity_food_for_every_order[0]

    if current_order < quantity_of_food_for_the_day:
        quantity_of_food_for_the_day -= current_order
        quantity_food_for_every_order.popleft()
    else:
        break
print(max_num)
if not quantity_food_for_every_order:
    print("Orders complete")
else:
    print(f"Orders left: {', '.join(map(str,quantity_food_for_every_order))}")