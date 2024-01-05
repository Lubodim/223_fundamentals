n= int(input())
matrix = [[int(x) for x in input().split(', ')]for _ in range(n)]

c = 2
result = float("inf")
min_matrix = []

for i in range(n - c + 1):
    for j in range(n - c + 1):
        sub_matrix = ([row[j:j + c]for row in matrix[i:i + c]])
        sum_sub_matrix = sum(sum(row) for row in sub_matrix)
        if sum_sub_matrix < result:
            result = sum_sub_matrix
            min_matrix = sub_matrix
for row in min_matrix:
    print(" ".join(map(str, row)))
print("min result", result)