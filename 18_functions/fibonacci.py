def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return "0"
    elif n == 2:
        return "0, 1"
    else:
        def fib_sequence(n, a=0, b=1):
            if n == 0:
                return []
            else:
                return [a] + fib_sequence(n - 1, b, a + b)

        sequence = fib_sequence(n)
        return ", ".join(str(x) for x in sequence)

num_terms = int(input("Въведете брой числа на Фибоначи: "))

fibonacci_sequence = fibonacci_recursive(num_terms)

print(f"Числата на Фибоначи до {num_terms}-то са: {fibonacci_sequence}")
