n = int(input())
my_set = set()
for i in range(n):
    number_of_command = input()

    if number_of_command not in my_set:
        my_set.add(number_of_command)
while True:
    invited_people = input()
    if invited_people == "END":
        break

    if invited_people in my_set:
        my_set.remove(invited_people)

print(len(my_set))
print("\n".join(my_set))