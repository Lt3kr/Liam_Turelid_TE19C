y=int(input("ge mig ett tal du vill vara burr: "))
z=int(input("ge mig ett tal du vill vara birr: ")) #ber om birr och burr
x=0

antalet_birr = 0
antalet_burr = 0 #skapar värden för antalet birr och burr


for i in range(101):
    if x % z == 0 and x % y == 0:
        print("birr and burr") #kollar efter birr och burr läger värden på det ifall det är sant
        antalet_birr += 1
        antalet_burr += 1
    elif x % z == 0:
        print("birr") #kollar birr och adderar birr
        antalet_birr += 1
    elif x % y != 0: #kollar ifall det inte är burr
        print(x)
    else:
        print("burr") #annars ifall ingen annan av funktionerna fungerar så är det burr och därmed lägger till värde på burr
        antalet_burr += 1
    x += 1

print(antalet_birr, antalet_burr) #skriver ut värderna utanför loopen