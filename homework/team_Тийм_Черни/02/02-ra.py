stack = []  # Инициализираме празен стек

n = int(input())  # Четем броя на командите

for _ in range(n):
    command = input().split()

    if command[0] == '1':
        number = int(command[1])
        stack.append(number)  # Добавяме числото най-отзад на стека
    elif command[0] == '2':
        if stack:
            stack.pop()  # Изтриваме числото, което е най-отгоре на стека
    elif command[0] == '3':
        if stack:
            print(max(stack))  # Извеждаме най-голямото число в стека
    elif command[0] == '4':
        if stack:
            print(min(stack))  # Извеждаме най-малкото число в стека
    elif command[0] == '5':
        print(len(stack))  # Извеждаме дължината на стека

# Изпразваме стека и го печатаме в обратен ред
stack.reverse()
print(', '.join(map(str, stack)))