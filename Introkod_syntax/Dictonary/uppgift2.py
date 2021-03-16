import random as rnd

antalsiffror = {}
for i in range(1, 7):
    antalsiffror[i] = 0 

    for i in range(100000):
        tärningskast = rnd.randint(1, 6)
        if tärningskast == 1:
            antalsiffror[1] += 1
        elif tärningskast == 2:
            antalsiffror[2] += 1
        elif tärningskast == 3:
            antalsiffror[3] += 1
        elif tärningskast == 4:
            antalsiffror[4] += 1
        elif tärningskast == 5:
            antalsiffror[5] += 1
        elif tärningskast == 6:
            antalsiffror[6] += 1

for siffror in antalsiffror:
    print(f"{siffror}: {antalsiffror[siffror]}")

#Viking hjälpte mig att förstå och det är därför det kan finnas liknelser