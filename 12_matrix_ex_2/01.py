row_col = int(input())
matrix=[]
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(row_col)
print(*matrix , sep="\n")
#4
1, 3, 0, 1
8, 2, 6, 2
1, 7, 6, 3
0, 4, 1, 4
