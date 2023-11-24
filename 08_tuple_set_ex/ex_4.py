some_string = input()
my_dict = {}
for letter in some_string:
    if letter not in my_dict:
        my_dict[letter] = 0
    my_dict[letter] += 1

for k, v in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
    print(f"{k}: {v} time/s")