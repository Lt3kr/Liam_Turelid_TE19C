#räkna ut 11 / 1 + 3.4e^-0.3t
import math

def population(t):
    x = 11 / (1 + 3.4*math.exp(-0.03*t))
    return x
print(f"populationen är {population(1)}")
