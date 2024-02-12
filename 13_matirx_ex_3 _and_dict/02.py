row_col = int(input())
matrix = []
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(row + 1)
print(*matrix, sep="\n")