num = int(input())
matrix = []

for i in range(num):
    matrix.append(list(map(int, input().split(","))))
for i in matrix:
    print(*i, sep=", ")