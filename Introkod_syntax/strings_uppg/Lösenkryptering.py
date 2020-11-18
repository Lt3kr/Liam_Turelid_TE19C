alfabetet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

ROTLösen = input("ROT och ditt lösen: ")

seperation = ROTLösen.split(" ")
ROT = int(seperation[0])
Meddelande = seperation[1].upper()

resultat = ""
for letter in Meddelande:
    PositonAvBokstav = alfabetet.index(letter)
    PositonAvBokstav += ROT
    while PositonAvBokstav > len(alfabetet) -1:
        PositonAvBokstav -= len(alfabetet)
    resultat += alfabetet[PositonAvBokstav]

print(resultat[::-1])