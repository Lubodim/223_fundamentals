food_quantity = int(input())
orders = list(map(int, input().split()))
largest_order = max(orders)
while orders:
    current_order = orders[0]

    if food_quantity >= current_order:
        food_quantity -= current_order
        orders.pop(0)
    else:
        break

if not orders:
    print(largest_order)
    print("Orders complete")
else:
    print(largest_order)
    remaining_orders = ', '.join(map(str, orders))
    print(f"Orders left: {remaining_orders}")