# punkt 1 = 3,3 och punkt 2 = -2,1

#vad är avståndet från origon, det är pythagoras sats
import math

Punkt = [3,3]
Punkt2 = [-2,1]

def avståndet(Punkt, Punkt2):
    return ((Punkt[0] - Punkt2[0])**2 + (Punkt[1] - Punkt2[1])**2)

sanna_avståndet = math.sqrt(avståndet(Punkt, Punkt2))

print(f"distans ifrån punkterna är {sanna_avståndet}")