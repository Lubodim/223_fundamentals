from collections import deque

number_of_commands = int(input())
stack = deque()
for commands in range(number_of_commands):
    try:

        numbers = input().split()
        if int(numbers[0]) == 1:
            number_for_deque = int(numbers[1])
            stack.append(number_for_deque)
        elif int(numbers[0]) == 2:
            stack.popleft()
        elif int(numbers[0]) == 3:
            print(max(stack))
        elif int(numbers[0]) == 4:
            print(min(stack))
        elif int(numbers[0]) == 5:
            print(len(stack))

    except IndexError:
        numbers = input().split()
        if int(numbers[0]) == 1:
            number_for_deque = int(numbers[1])
            stack.append(number_for_deque)
        elif int(numbers[0]) == 2:
            stack.popleft()
        elif int(numbers[0]) == 3:
            print(max(stack))
        elif int(numbers[0]) == 4:
            print(min(stack))
        elif int(numbers[0]) == 5:
            print(len(stack))

stack.reverse()
# print(*stack)
print(", ".join(map(str, stack)))