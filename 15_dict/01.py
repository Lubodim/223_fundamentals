data = input().split()
class_223 = {}

for el in range(0, len(data), 2):
    name = data[el]
    number = int(data[el + 1])

    if name not in class_223.keys():
        class_223[name] = number
print(class_223)