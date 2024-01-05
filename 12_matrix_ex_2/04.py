row_col = int(input())
# matrix = []
total_sum = 0
for _ in range(row_col):
    current_row = list(map(int, input().split(", ")))
    # current_row = [int(x) for x in input().split(", ")]
    # matrix.append(current_row)
    total_sum += sum(current_row)
# print(*matrix, sep='\n')
# for r in matrix:
#     total_sum += sum(r)
print(total_sum)