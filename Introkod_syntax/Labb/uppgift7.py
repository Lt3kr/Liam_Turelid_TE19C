import math
import random as rnd
import matplotlib.pyplot as plt

x = rnd.uniform(-1, 1) #gör ett random tal med decimaler mellan -1 och 1
y = rnd.uniform(-1, 1) #gör samma fast för en annan variabel

cricle = plt.Circle((0,0), radius=1, color="red") #skapar en cirkel med radien 1 och är färgad röd
rectangle = plt.Rectangle((-1,-1), width=2, height=2, color="blue") #skapar en blå rektangel
ax = plt.gca() #gör en variabel som ritar ut former
avståndet = x**2 + y**2 
t=0

y_värde = [] #skapar tomma arrayer som så jag kan lägga i värden i
x_värde = [] #gör samma fast för en annan array

for i in range(10):
    x = rnd.uniform(-1, 1)
    y = rnd.uniform(-1, 1)
    avståndet = x**2 + y**2
    x_värde.append(x)
    y_värde.append(y) #räknar ut allt flera gånger med olika värden

print(x_värde, y_värde)

ax.add_patch(rectangle) #ritar ut rektangeln över hela grafen
ax.add_patch(cricle) #ritar cirkeln
plt.plot(x_värde, y_värde, '*') #sätter ut alla olika punkter
plt.show()

#uppgift H: jag vet inte ifall det här är svaret du söker men jag märker med olika radier på circeln så är sanolikheten att det är endast en viss mängd med punkter i cirkel t.ex så hade 0.5 radien nästan alltid 2 punkter.