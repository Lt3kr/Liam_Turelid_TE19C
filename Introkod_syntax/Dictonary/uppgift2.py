import random as rnd

x = 0

for i in range(100000):
    tärningskast = rnd.randint(1, 6)
    if tärningskast == 1:
        x += 1
    elif tärningskast == 2:
        x += 1

Olikatärningskast = {
    
}

print(x)