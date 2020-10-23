import math
import random as rnd

x = rnd.uniform(-1, 1)
y = rnd.uniform(-1, 1)

avståndet = x**2 + y**2
t=0


for i in range(100000):
    x = rnd.uniform(-1, 1)
    y = rnd.uniform(-1, 1)
    avståndet = x**2 + y**2
    if math.sqrt(avståndet) <= 1:
        t += 1

print(f"{(t/100000)*4}") #den kommer närmare pi desto mer gånger man testar