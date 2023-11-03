numbers = tuple([float(digit) for digit in input().split(" ")])
# numbers = tuple(map(float, input().split(" ")))
my_dict = {}

for dg in numbers:
    if dg not in my_dict:
        my_dict[dg] = 0
    my_dict[dg] += 1

for k, v in my_dict.items():
    print(f"{k} - {v} times")

