from collections import deque
the_biggest_order = 0
deque_of_orders = deque()
total_quantity_of_food = 0
quantity_of_food = int(input())
list_of_food_of_every_order = input().split()
for food in list_of_food_of_every_order:
    if int(food) > the_biggest_order:
        the_biggest_order = int(food)
    deque_of_orders.append(int(food))

print(the_biggest_order)

while deque_of_orders:
    first_order = deque_of_orders.popleft()
    total_quantity_of_food += first_order
    last_element = len(deque_of_orders) == 0
    if total_quantity_of_food <= quantity_of_food:
        if last_element:
            print("Orders complete")
    elif total_quantity_of_food > quantity_of_food:
        element_of_deque_as_string = [str(element) for element in deque_of_orders]
        print(f"Orders left: {first_order}, {', '.join(element_of_deque_as_string)}")
        break
