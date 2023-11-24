invited = set()
n = int(input("Enter a number: "))
for _ in range(n):
    code = input("Enter code: ")
    invited.add(code)
while True:
    command = input()
    if command == "END":
        break
    invited.discard(command)

print(len(invited))

number_starting_codes = [code for code in invited if code[0].isdigit()]
other_codes = [code for code in invited if not code[0].isdigit()]

for code in number_starting_codes + other_codes:
    print(code)








