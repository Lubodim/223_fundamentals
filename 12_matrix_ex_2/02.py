row_col = int(input())
matrix = []
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(row + 1)
for row in matrix:
    print(*row, sep = ", ")