rc = int(input())
print(*[[(col + 1 + row * rc) for col in range(rc)] for row in range(rc)], sep="\n")

# matr = []
# r_c = int(input())
# for row in range(r_c):
#     matr.append([])
#     for col in range(r_c):
#         matr[row].append(col + 1 + row * r_c)
# print(*matr, sep='\n')