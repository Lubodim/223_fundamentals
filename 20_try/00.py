class Spiridon(Exception):
    pass
def something(n):
    for i in range(n):
        if i == 2:
            raise Spiridon("I o6te kak")
        if i == 5:
            raise ValueError("Invalid number")
    return "fun"
try:
    print(something(10))
except ValueError as ve:
    print("Mnogo losho - ", ve)
except Spiridon as sp:
    print("Towa e qko - ", sp)
else:
    print("Something happened well!")
finally:
    print("That was everything for now")