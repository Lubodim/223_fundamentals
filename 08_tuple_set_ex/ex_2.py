m, n = tuple(map(int, input().split(" ")))

# comand = input().split()
# m = int(comand[0])
# n = int(comand[1])
set_m = set()
set_n = set()


for i in range(m):
    numb = int(input())
    set_m.add(numb)

for _ in range(n):
    set_n.add(int(input()))

print(set_m)
print(set_n)
print()
print(*set_m.intersection(set_n), sep="\n")