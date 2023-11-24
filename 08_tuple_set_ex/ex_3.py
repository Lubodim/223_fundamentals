n = int(input())
my_set = set()

for _ in range(n):
    baby_lang = input().split(' ')
    for lang in baby_lang:
        my_set.add(lang)

while my_set:
    print(my_set.pop())
