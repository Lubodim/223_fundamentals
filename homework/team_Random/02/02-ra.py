my_stack = []
n = int(input())
digits = 0
for i in range(n):
    text = input().split()
    command = int(text[0])
    if len(text) > 1:
        digits = int(text[1])
    if command == 1:
        my_stack.append(digits)
    if my_stack:
        if command == 2:
            my_stack.pop()
        elif command == 3:
            print(max(my_stack))
        elif command == 4:
            print(min(my_stack))
    if command == 5:
        print(len(my_stack))

print(*my_stack[::-1], sep=", ")