import random as rnd

allaKast = []
HurMångaFemmor = 0

with open("diceRoll.txt", "w"):
    for i in range(10):
        tärningskast = rnd.randint(1, 6)
        allaKast.append(tärningskast)
    print(allaKast)
    print(sorted(allaKast))
    for i in range(allaKast.__len__):
    