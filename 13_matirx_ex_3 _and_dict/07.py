# rows, cols = map(int, input().split(", "))
rows, cols = [int(x) for x in input().split(", ")]

# cols = int(cols)
matrix = []

for _ in range(rows):
    matrix.append(input().split(", "))

searched_symbol = input()

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == searched_symbol:
            print(f"{r}, {c}")
