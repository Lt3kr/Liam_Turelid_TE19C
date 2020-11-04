import math
import random as rnd
import matplotlib.pyplot as plt

x = rnd.uniform(-1, 1)
y = rnd.uniform(-1, 1)

cricle = plt.Circle((0,0), radius=1, color="red")
rectangle = plt.Rectangle((-1,-1), width=2, height=2, color="blue")
ax = plt.gca()
avståndet = x**2 + y**2
t=0

y_värde = []
x_värde = []

for i in range(10):
    x = rnd.uniform(-1, 1)
    y = rnd.uniform(-1, 1)
    avståndet = x**2 + y**2
    x_värde.append(x)
    y_värde.append(y)

print(x_värde, y_värde)

ax.add_patch(rectangle)
ax.add_patch(cricle)
plt.plot(x_värde, y_värde, '*')
plt.show()

#uppgift H: jag vet inte ifall det här är svaret du söker men jag märker med olika radier på circeln så är sanolikheten att det är endast en viss mängd med punkter i cirkel t.ex så hade 0.5 radien nästan alltid 2 punkter.