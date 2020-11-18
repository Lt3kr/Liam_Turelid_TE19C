alfabetet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

LösenordOchROT = input("skriv ROT nummer mellanslag Lösen: ")

Seperation = LösenordOchROT.split(" ")
ROTNummer = int(Seperation[0])
Lösen = Seperation[1].upper()

RiktigaLösen = ""
for letter in Lösen:
    Position = alfabetet.index(letter)
    Position -= ROTNummer
    while Position > len(alfabetet) -1:
        Position -= len(alfabetet)
    RiktigaLösen += alfabetet[Position]

print(RiktigaLösen[::-1])

