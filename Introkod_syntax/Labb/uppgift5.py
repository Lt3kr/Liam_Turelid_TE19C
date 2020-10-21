#simulera flera punkter de som hamnar i cirkeln dividerat på antalet som kastats
import math
import random as rnd

x = rnd.uniform(-1, 1)
y = rnd.uniform(-1, 1)

avståndet = x**2 + y**2
t=0

for i in range(10): #görs 10ggr
    x = rnd.uniform(-1, 1) #ger x ett värde mellan -1 och 1
    y = rnd.uniform(-1, 1) #ger y ett värde mellan -1 och 1
    avståndet = x**2 + y**2 #pythagoras sats för att börjaräkna ut avstånd
    if math.sqrt(avståndet) <= 1: #gör if-sats där den endas räknar med avständet om det är under cirkelns diameter alltså innanför cirkeln
        t += 1 #lägger till ett för antal träffar i t och adderar dem

print(f"{t/10}") #divideras med antalet kastningar