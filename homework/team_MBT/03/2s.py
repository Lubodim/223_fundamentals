num = int(input())
grades_dict = {}
for i in range(num):
    name, grade = tuple([digit for digit in input().split()])
    grade = float(grade)

    if name not in grades_dict:
        grades_dict[name] = []

    grades_dict[name].append(grade)

for names, grades in grades_dict.items():
    print(f"{names} -> {' '.join([f'{grad:.2f}' for grad in grades])} (avg: {sum(grades) / len(grades):.2f})")

# num = int(input())
# grades_dict = {}
# for i in range(num):
#    name, grade = input().split()
#    grade = float(grade)
#
#    if name not in grades_dict:
#        grades_dict[name] = []
#
#    grades_dict[name].append(grade)
#
# for names, grades in grades_dict.items():
#    print(f"{names} -> {' '.join([f'{grad:.2f}' for grad in grades])} (avg: {sum(grades) / len(grades):.2f})")
