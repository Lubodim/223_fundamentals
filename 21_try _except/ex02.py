def sum_list(lst):
    if not lst:
        raise IndexError
    total = 0
    for number in lst:
        total += int(number)
    return total
try:
    data = input().split()
    print(sum_list(data))
except ValueError:
    print("You can not sum int and str")
except IndexError:
    print("You can not sum empty list")