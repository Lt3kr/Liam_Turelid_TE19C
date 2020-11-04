Start = int(input("Ge mig ett tal som jag ska börja vid: "))
Stop = int(input("Ge mig ett tal som jag ska sluta vid: "))
Multipel_burr = int(input("Ge mig multipeln som är burr: "))
Multipel_birr = int(input("Ge mig multipeln som ska vara birr: "))

x = Start

for i in range(Start, Stop + 1):
    if x % Multipel_birr == 0 and x % Multipel_burr == 0:
        print(f"{x} birr and burr")
    elif x % Multipel_burr == 0:
        print("burr")
    elif x % Multipel_birr == 0:
        print("birr")
    else:
        print(x)
    x += 1

