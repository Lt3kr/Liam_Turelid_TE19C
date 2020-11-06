Start = int(input("Ge mig ett tal som jag ska börja vid: "))
Stop = int(input("Ge mig ett tal som jag ska sluta vid: "))
Multipel_burr = int(input("Ge mig multipeln som är burr: "))
Multipel_birr = int(input("Ge mig multipeln som ska vara birr: ")) #ber en att sätta in alla värden

x = Start #gör så att x börjar som start hela tiden

for i in range(Start, Stop + 1):
    if x % Multipel_birr == 0 and x % Multipel_burr == 0: #kollar om det är burr birr sedan printar om det är det
        print(f"{x} birr and burr")
    elif x % Multipel_burr == 0: #kollar burr
        print("burr")
    elif x % Multipel_birr == 0: #kollar birr
        print("birr")
    else:
        print(x) #annars printar det bara det talet det är på, att skriva så här resulterar i att talet endast skrivs ifall inget annat aktiveras
    x += 1

