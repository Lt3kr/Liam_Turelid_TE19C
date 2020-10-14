import matplotlib.pyplot as plt
import numpy as np

y_sträcka = [10,20,30,40,50,60,70,80,90,100]
x_tid = [1.83, 2.87, 3.78, 4.65, 5.5, 6.23, 7.14, 7.96, 8.79, 9.69]
v = []

for i in range(1,len(y_sträcka)):
    v.append((y_sträcka[i]-y_sträcka[i-1])/(x_tid[i]-x_tid[i-1]))

print(v)

plt.plot(v)
plt.show()