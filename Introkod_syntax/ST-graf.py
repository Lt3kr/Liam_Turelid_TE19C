import matplotlib.pyplot as plt
import numpy as np

y_sträcka = [0,10,20,30,40,50,60,70,80,90,100]
x_tid = [0, 1.83, 2.87, 3.78, 4.65, 5.5, 6.32, 7.14, 7.96, 8.79, 9.69]
v = [0]

for i in range(1,len(x_tid)):
    v_i = ((y_sträcka[i]-y_sträcka[i-1])/(x_tid[i]-x_tid[i-1]))
    v.append(v_i)

plt.plot(x_tid, v, '.-')
plt.title("Usain bolt 100 meters V-T graf")
plt.xlabel("Tid i sek")
plt.ylabel("Hastighet i m/s")
plt.show()