import cowsay
print(cowsay.ghostbusters("GAME - Guess the number - created by 22305"))
winning = ["a", "b", "c", "d"]
account = int(input("Account money: "))
zalog = int(input("Bet: "))

while True:
    account -= zalog
    print()
    command = input("Enter a symbol: ")
    if command == "Stop":
        break
    if command.lower() in winning:
        account += zalog
        print("Congratulations you WON!!!")
        print(f"your money now are {account * 2}")
        break
    else:
        print()
        print("Try again :) give me your last money!")
    print(f"Now you have {account} leva")