my_dict = {}
txt = input()
for i in range(len(txt)):
    if txt[i] not in my_dict:
        my_dict[txt[i]] = 0
    my_dict[txt[i]] += 1
for k, v in sorted(my_dict.items()):
    print(f"{k}: {v} time/s")