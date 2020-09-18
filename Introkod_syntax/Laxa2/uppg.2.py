#Gör ett program som skriver ut ifall det jämt, udda eller delbart med 5

Tal = float(input("Skriv ditt tal så ska jag se ifall det är delbart med 5 och som en liten bonus så ska jag också kolla ifall det är jämt eller udda: "))

if Tal %5 == 0:
    print("Det är delbart med 5!")
elif Tal % 2 == 0:
    print("Det är ett jämt tal!")
else:
    print("Det är ett udda tal!")