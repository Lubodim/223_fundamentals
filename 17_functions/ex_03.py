
list = [float(x) for x in input().split()]
abs_list = []
cc = lambda x: abs(x)
for i in list:
   abs_list.append(cc(i))

print(abs_list)

