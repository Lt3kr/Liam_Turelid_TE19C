import random as rnd

antalsiffror = {}
for i in range(1,6):
    antalsiffror[i:] = 0 
    for i in range(100000):
        tärningskast = rnd.randint(1, 6)
        if tärningskast == 1:
            antalsiffror[1:] += 1
        elif tärningskast == 2:
            antalsiffror[2:] += 1
print(f"Så här många tvåor och ettor var det: ")
for key in antalsiffror:
    print(key, antalsiffror[key])