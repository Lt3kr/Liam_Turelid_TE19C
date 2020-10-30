y=int(input("ge mig ett tal du vill vara burr: "))
z=int(input("ge mig ett tal du vill vara birr: "))
x=0

for i in range(100):
    x += 1
    if x % z == 0:
        print("birr")
    elif x % y != 0:
        print(x)
    else:
        print("burr")