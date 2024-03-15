def class_room(**students):
    string = ''
    for student,grades in students.items():
        string += f"{student}\n"
        for grade in grades:
            string += f"{grade}\n"
    return string




print(
    class_room(
        Спиридон=[2, 3, 3, 4, 6],
        Стамат=[6, 6, 6, 2],
        Анджелина=[3, 3, 4, 3, 5]
    )
)
