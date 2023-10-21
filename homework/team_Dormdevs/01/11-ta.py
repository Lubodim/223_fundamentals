players_names = input().split(" ")
n_throwing = int(input())
current_player = 0
while True:
    if len(players_names) == 1:
        break
    current_player = (n_throwing + current_player - 1) % len(players_names)
    removed_player = players_names.pop(current_player)
    print(f"Removed {removed_player}")

print(f"Last is {players_names[0]}")