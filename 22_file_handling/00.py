# Задача 1
with open("output.txt", "w") as f:
    f.write("Текст, който ще бъде записан във файла.\n")

with open("output.txt", "r") as f:
    print(f.read())

# Задача 2
with open("data.txt", "a") as f:
    while True:
        user_input = input("Въведете текст (за край въведете 'end'): ")
        if user_input == "end":
            break
        f.write(f"{user_input}\n")

with open("data.txt", "r") as f:
    print(f.read())

# Задача 3
import os

if not os.path.exists("test.txt"):
    with open("test.txt", "w") as f:
        f.write("Съдържание на новия файл.")
else:
    os.remove("test.txt")
    with open("test.txt", "w") as f:
        f.write("Ново съдържание след изтриване на старото.")


# Задача 4
with open("numbers.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i}\n")

# Задача 5

with open("data.txt", "r") as f_input:
    data = f_input.read()

clean_data = ''.join(char for char in data if char.isalnum() or char in [' ', '\n'])

with open("clean_data.txt", "w") as f_output:
    f_output.write(clean_data)



import os

if not os.path.exists("log.txt"):
    with open("log.txt", "w") as f:
        f.write("Стартиране на програмата.\n")
else:
    with open("log.txt", "a") as f:
        f.write("Текущо изпълнение на програмата.\n")



# Задача 7
import os
from datetime import datetime

if os.path.exists("temp.txt"):
    os.remove("temp.txt")

with open("temp.txt", "w") as f:
    f.write(str(datetime.now()))

# Задача 8
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as f3:
    for line in f1:
        f3.write(line)
    for line in f2:
        f3.write(line)

# Задача 9
with open("data.txt", "r") as f:
    words = f.read().split()

print(f"Брой думи във файла са {len(words)}")


# Задача 10
with open("input.txt", "r") as f_input, open("output.txt", "w") as f_output:
    for line in f_input:
        if line.startswith("A"):
            f_output.write(line)

