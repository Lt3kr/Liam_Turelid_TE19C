import random as rnd

allaKast = []
HurMångaFemmor = 0

for i in range(10):
    tärningskast = rnd.randint(1, 6)
    allaKast.append(tärningskast)
print(allaKast)
print(sorted(allaKast))
for i in allaKast:
    if i == 5:
        HurMångaFemmor += 1
print(HurMångaFemmor)


with open("diceRoll.txt", "w") as diceRoll:
    diceRoll.write("Alla kasten " + str(allaKast) + "\n")
    diceRoll.write("De sorterade kasten " + str(sorted(allaKast)) + "\n")
    diceRoll.write("Hur många femmor " + str(HurMångaFemmor))
    diceRoll.close()