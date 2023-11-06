total_sum = 0
total_sum_even = 0
total_sum_odd = 0
range_num = int(input())

for i in range(1, range_num + 1 ):
    total_sum += i
    if i % 2 == 0:
        total_sum_even += i
    else:
        total_sum_odd += i
print(total_sum)
print(total_sum_even)
print(total_sum_odd)