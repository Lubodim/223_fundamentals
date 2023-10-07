import cowsay
print(cowsay.ghostbusters("GAME - Guess the number - created by 22105"))

from random import sample
from string import ascii_letters, digits, punctuation
all_combinations = ascii_letters + digits + punctuation
count = 0
# password_length = int(input("Enter your password length: "))
password_length = 20

for p in range(0, 200):
    count += 1

    password = ''.join(sample(all_combinations, password_length))
    print(f"{count} Your password is: {password}")
