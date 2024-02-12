from random import choice
from _collections import deque
from time import sleep
fighters = deque([
    "Scorpion", "Liu Kang", "Sub Zero", "Kano",
    "Sonya Blade", "Raiden", "Baraka", "Jax",
    "Johnny Cage", "Kung Lao", "Jade",
    "Noob Saibot", "Kabal", "Geras", "D'Vorah",
    "Jacqui Briggs", "Scarlett", "Cassie Cage",
    "Kotal Kahn", "Erron Black"
])
killed = []
player = input("Enter your name: ")
player_health = 100
player_shield = 80
player_power = 70

print("Welcome to the game Mortral Combat!")

is_continued = False
while True:
    if player_health <= 0:
        print(f"{player} has killed {', '.join(killed)}")
        print("Game over!")
        break
    if is_continued:
        while True:
            question = input("Do you want to continue fight Y/N? ").upper()
            if question == "Y":
                break
            elif question == "N":
                print(f"{player} has killed {', '.join(killed)}")
                exit()
            else:
                print("Incorrect answer")
                continue
    is_continued = True
    if fighters:
        comp = fighters.popleft()
    else:
        print(f"{player} has killed {', '.join(killed)}")
        print("That was everyone\nCongratulations you WIN!!!")
        exit()
    comp_health = 100
    comp_shield = choice(range(20, 80))
    comp_power = choice(range(20, 80))
    player_health = 100
    if killed:
        if len(killed) % 3 == 0:
            player_health += (10 * len(killed)//3)
            player_shield -= 4
            player_power -= 4
            comp_power += 4
            comp_shield += 4
            comp_health += 10
    print("Loading...", end="")
    sleep(3)
    for _ in range(5):
        print(".", end="")
        sleep(2)
    print()
    print()
    print(f"{player} have {player_shield} shield, {player_health} health {player_power} power.")
    print()
    print(f"{comp} have {comp_shield} shield, {comp_health} health {comp_power} power.")
    print()
    while True:
        print(f"{player} will hit {comp}")
        print(f"{comp} before hit have {comp_health}")
        sleep(3)
        print()
        if player_power >= comp_shield:
            comp_health -= (player_power - comp_shield)
        else:
            comp_health -= player_power//6
        print(f"{comp} after hit have {comp_health}")
        print()
        if comp_health <=0:
            print(f"{comp} was killed by {player}")
            killed.append(comp)
            break
        print(f"{comp} will hit {player}")
        print(f"{player} before hit have {player_health}")
        sleep(3)
        print()
        if comp_power >= player_shield:
            player_health -= (comp_power - player_shield)
        else:
            player_health -= comp_power // 6
        print(f"{player} after hit have {player_health}")
        print()
        if player_health <= 0:
            print(f"{player} has killed {', '.join(killed)}")
            print("Game over!")
            exit()
        player_shield += 3
        player_power += 3

