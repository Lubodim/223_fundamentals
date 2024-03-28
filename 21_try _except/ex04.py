def dict_work(da,name):
    results=[]
    my_dict = {}
    for i in range(0, len(da) ,2):
        my_dict[da[i]] = int(da[i+1])
    for n in name:
        results.append(my_dict[n])
    return results



data =input().split()
names = input().split(", ")
try:
    print(*dict_work(data,names) ,sep=", ")
except KeyError:
    print("This person does not exist")
else:
    print("That was the ages of the person")

