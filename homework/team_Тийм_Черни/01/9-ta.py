opashka = []

while True:
    klienti = input()

    if klienti == "END".lower():
        remaining_people = len(opashka)
        if remaining_people > 0:
            for people01 in opashka:
                print(people01)
            print(f"{remaining_people} people remaining.")
        else:
            print("0 people remaining.")
        break

    elif klienti == "PAID".lower():
        while opashka:
            print(opashka.pop(0))
    else:
        opashka.append(klienti)
