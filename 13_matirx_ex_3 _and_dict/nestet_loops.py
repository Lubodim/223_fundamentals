from time import sleep
days = 0
while True:
    for h in range(24):
        for m in range(60):
            for s in range(60):
                print(f"{days:010d}{h:02d}:{m:02d}:{s:02d}")
    days += 1
