cars = int(input())  # тук се въвежда колко коли изкам да вкарам
entries = set()  # това е мястото което се поставя колата

for _ in range(cars):
    in_out, car_numbers = input("Enter IN/OUT and car number separated by comma: ").split(
        ',')  # ту проверяваме дали има нещо в cars и със split си разделяме колите на вход изход и номер и се активира

    if in_out.lower() == "in":  #
        entries.add(car_numbers)

    elif car_numbers not in entries:  #
        print("False")

    elif len(car_numbers) != 8:
        print('invalid car number')

    else:  #
        print("Invalid in/out")

while entries:  #
    if not entries:  #
        print("No entries")
    else:
        print(entries.pop())
