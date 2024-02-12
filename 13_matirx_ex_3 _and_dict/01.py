a = int(input())
matrix = []
counter = 1
for i in range(a):
    matrix.append([])
    for j in range(a):
        matrix[i].append(counter)
        counter += 1
print(*matrix, sep='\n')
