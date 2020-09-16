#gör en if sats som printar ut ifall det givna numret är positivt, negativt eller noll

nr = float(input("skriv ett nummer så ska jag se om det är +, - eller noll: "))

if nr > 0:
    print("Ditt nummer är positivt")
elif nr == 0:
    print("Ditt nummer är noll")
else:
    print("Ditt nummer är negativt")