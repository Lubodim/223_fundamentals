# n= int(input())
# matrix = [[int(x) for x in input().split(', ')]for _ in range(n)]
#
# c = 2
# result = float("inf")
# min_matrix = []
#
# for i in range(n - c + 1):
#     for j in range(n - c + 1):
#         sub_matrix = ([row[j:j + c]for row in matrix[i:i + c]])
#         sum_sub_matrix = sum(sum(row) for row in sub_matrix)
#         if sum_sub_matrix < result:
#             result = sum_sub_matrix
#             min_matrix = sub_matrix
# for row in min_matrix:
#     print(" ".join(map(str, row)))
# print("min result", result)



n, m = map(int, input().split(", "))
matrix = [[int(x) for x in input().split(', ')]for _ in range(n)]

result = float("inf")
min_matrix = []

for r in range(n - 1):
    for c in range(n - 1):
        current_element = matrix[r][c]
        left_element = matrix[r][c + 1]
        down_element = matrix[r + 1][c]
        down_left_element = matrix[r + 1][c + 1]
        current_sum = current_element + left_element + down_element +down_left_element
        sub_matrix = [current_element, left_element, down_element, down_left_element]
        if current_sum < result:
            result = current_sum
            min_matrix = sub_matrix
for i, el in enumerate(min_matrix):
    if i % 2 == 0:
        print(el, end=' ')
    else:
        print(el)
print("Min result", result)