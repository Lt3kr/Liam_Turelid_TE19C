import math
import random as rnd
import matplotlib.pyplot as plt

x = rnd.uniform(-1, 1)
y = rnd.uniform(-1, 1)

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

circle = plt.Circle((0.0), 1, color='r')
plt.plot(x_värde, y_värde)
plt.show()