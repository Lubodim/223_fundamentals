stack = []

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == '1':
        num = int(command[1])
        stack.append(num)
    elif command[0] == '2':
        if stack:
            stack.pop()
    elif command[0] == '3':
        if stack:
            print(max(stack))
    elif command[0] == '4':
        if stack:
            print(min(stack))
    elif command[0] == '5':
        print(len(stack))

while stack:
    print(stack.pop(), end=", ")
