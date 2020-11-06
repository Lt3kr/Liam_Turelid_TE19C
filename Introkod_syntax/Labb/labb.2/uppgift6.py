Start = int(input("Ge mig ett tal som jag ska börja vid: "))
Stop = int(input("Ge mig ett tal som jag ska sluta vid: "))
Multipel_burr = int(input("Ge mig multipeln som är burr: "))
Multipel_birr = int(input("Ge mig multipeln som ska vara birr: "))

x = Start


if Start - Stop >= 0:
    print("du kan inte börja på ett tal större än slutet") #fel hantering där man inte kan ha ett startvädre mindre än sluvärdet
elif Start < 0:
    print("Du får inte starta på ett negativt tal") #fel hantering som kollar ifall start  värdet är mindre än 0 och säger att det inte kan vara det
else:
    for i in range(Start, Stop + 1):
        if x % Multipel_birr == 0 and x % Multipel_burr == 0:
            print("birr and burr")
        elif x % Multipel_burr == 0:
            print("burr")
        elif x % Multipel_birr == 0:
            print("birr")
        else:
            print(x)
        x += 1
