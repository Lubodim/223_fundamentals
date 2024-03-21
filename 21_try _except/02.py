class Galq(Exception):
    pass

def sum_func(lst):
    if len(lst) == 1 and type(lst[0]) == str:
        raise Galq
    if not lst:
        raise IndexError
    total = 0
    for el in lst:
        total += int(el)
    return total
my_list = input().split()

try:
    print(sum_func(my_list))
except ValueError:
    print("You can not sum int and str!")
except IndexError:
    print("You can not sum empty list!")
except Galq:
    print("Galya told me to do this")