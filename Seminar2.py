import random

def task1(n):
    coins = [];
    eagleCount = 0
    tailsCount = 0
    for i in range(n):
        coins.append(random.randint(0,1))
        if coins[i] == 0:
            eagleCount+=1
        else:
            tailsCount+=1
    return min(eagleCount, tailsCount)

n = int(input("Input count of coins\n"))
print(f"You need to turn over {task1(n)} coins")
