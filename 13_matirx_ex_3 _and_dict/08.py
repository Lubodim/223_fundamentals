rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

sub_matrix = []
max_sum = float("-inf")

for r in range(rows - 1):
    for c in range(cols - 1):
        current_element = matrix[r][c]
        right_element = matrix[r][c + 1]
        down_element = matrix[r + 1][c]
        down_right_element = matrix[r + 1][c + 1]
        current_sum = current_element + right_element + down_element + down_right_element
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [current_element, right_element, down_element, down_right_element]

for i, el in enumerate(sub_matrix):
    if i % 2 == 1:
        print(el)
    else:
        print(el, end=' ')

print(max_sum)