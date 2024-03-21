def dict_work(da, name):
    result = []
    my_dict = {}
    for i in range(0, len(da), 2):
        my_dict[da[i]] = int(da[i + 1])
    for n in name:
        result.append(my_dict[n])
    return result

data = input().split()
names = input().split(", ")
try:
    print(*dict_work(data, names), sep=", ")
except KeyError:
    print("This person does not exist in this dictionary")
else:
    print("That was ages of the persons")