from random import randint

print("Welcome to game for that who is today's choiced")

print()
class_members = int(input("Please enter a number of class members: "))

this_class = [int(x) for x in range(1, class_members + 1)]
# this_class_a = []
# for member in range(1, class_members + 1):
#
#     this_class_a.append(int(clas))



# print(','.join([str(x) for x in range(1, 31)]))
# sick_students = input('Please enter a sick Students in the following format: 11, 22,: ')
today_sick = [int(x) for x in input('Please enter a sick Students in the following format: 11, 22,: ').split(', ')]
for sick in today_sick:
    if sick in this_class:
        this_class.remove(sick)


flag = False
while this_class:
    print()
    if not flag:
        flag = True
        print("Would you like to start testing the class, by random number?")
    else:
        print("Will there be a next tested student?")
    command = input("Enter 'YES' or 'NO' to continue: ").upper()
    if command == 'NO':
        break
    elif command != 'YES' and command != 'NO':
        print()
        print("Your choice must be 'YES' or 'NO'")
        continue
    computer_choice = randint(1, class_members)

    if computer_choice not in this_class:
        continue
    else:
        this_class.remove(computer_choice)
    if computer_choice in today_sick:
        continue
    print(f"The student that will be tested now is: {computer_choice}")
    print(f"Left students for testing are: ")
    print(', '.join(str(x) for x in this_class))



