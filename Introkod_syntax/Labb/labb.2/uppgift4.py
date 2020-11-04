y=int(input("ge mig ett tal du vill vara burr: "))
z=int(input("ge mig ett tal du vill vara birr: "))
x=0

antalet_birr = 0
antalet_burr = 0


for i in range(101):
    if x % z == 0 and x % y == 0:
        print("birr and burr")
        antalet_birr += 1
        antalet_burr += 1
    elif x % z == 0:
        print("birr")
        antalet_birr += 1
    elif x % y != 0:
        print(x)
    else:
        print("burr")
        antalet_burr += 1
    x += 1

print(antalet_birr, antalet_burr)