y=int(input("ge mig ett tal du vill vara burr: "))
x=0

for i in range(100):
    x += 1
    if x % y != 0:
        print(x)
    else:
        print("burr")