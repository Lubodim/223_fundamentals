def sum_func(*args):
    final_sum = 0
    for element in args:
        if element % 2 ==0:
            final_sum += element
    return final_sum





print(sum_func(1, 4, 5))
print(sum_func(4, 5, 6, 1, 3))
print(sum_func(2, 20, 10, 15, 28, 3, 1))
