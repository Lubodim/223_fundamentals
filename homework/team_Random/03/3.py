n = int(input())
inv = set()
for i in range(n):
    code = input()
    inv.add(code)
arrivals = set()
while True:
    guest = input()
    if guest == "END":
        break
    arrivals.add(guest)
missing_guests = inv - arrivals
print(len(missing_guests))
for guest in missing_guests:
    print(guest)
