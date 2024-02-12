row_col = int(input())
matrix =[]
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(col+1+row*row_col)
print(*matrix ,sep= "\n")
