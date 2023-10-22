names_of_the_people = input().split()
number = int(input())
current_index = 0

while len(names_of_the_people) > 1:
    current_index = (current_index + number - 1) % len(names_of_the_people)
    remove = names_of_the_people.pop(current_index)
    print(f"Removed {remove}")
the_last_person = names_of_the_people[0]
print(f"The winner is {the_last_person}.")

