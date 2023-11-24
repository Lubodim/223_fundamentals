count_of_people = int(input())
invitation_numbers = set()

for person in range(count_of_people):
    invitation_number = input()
    invitation_numbers.add(invitation_number)

while True:
    a = input()
    if a == "END":
        break
    if a in invitation_numbers:
        invitation_numbers.remove(a)

print(len(invitation_numbers))
print(*sorted(invitation_numbers))
