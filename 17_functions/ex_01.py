num, num_2 = input().split(", ")

def power(a, b):
    result = a ** b
    return result
print(f"{num} to the power {num_2} is {power(int(num), int(num_2))}")