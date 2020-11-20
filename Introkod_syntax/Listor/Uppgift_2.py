import random

enLista = []

for i in range(10):
    x = random.randint(1, 6)
    enLista.append(x)

enLista.sort()

enLista.reverse()

print(enLista)