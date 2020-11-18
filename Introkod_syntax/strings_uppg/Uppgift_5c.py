fråga = input("kryptera eller dekryptera?: ")

alfabetet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

if fråga == "kryptera":

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
elif fråga == "dekryptera":
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
else:
    print("Endast kryptera eller dekrytera")