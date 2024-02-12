products = input().split()
order = input().split()
bar_dict = {}

for i in range(0, len(products), 2):
    product_name = products[i]
    quantity = int(products[i + 1])
    if product_name not in bar_dict.keys():
        bar_dict[product_name] = 0
    bar_dict[product_name] += quantity

print(bar_dict)