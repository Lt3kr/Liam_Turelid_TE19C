import random as rnd

y = 0
for i in range(1001):
    x = rnd.randint(1,6)
    if x == 5:
        y+=1

    print(x)
print(f"Det är exakt {y} gånger som tärningen blev 5")